#!/usr/bin/env python3
"""Build an enriched ACS locker directory. Public directory != live locker availability."""
import csv, datetime as dt, json, os, re, unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

ROOT='https://www.acscourier.net/el/acs-lockers/'
OUT=Path(__file__).with_name('acs-lockers.json')
OVERRIDES=Path(__file__).with_name('acs-locker-overrides.csv')
# Optional *merchant-provided* second locker dataset; never embed API credentials.
SECOND_URL=os.getenv('ACS_SECOND_SOURCE_URL','').strip()
HEADERS={'User-Agent':'Mozilla/5.0 (compatible; acs-locker-directory-sync/2.0)'}

def text(el): return re.sub(r'\s+',' ',el.get_text(' ',strip=True)).strip() if el else ''
def get(url):
    r=requests.get(url,timeout=40,headers=HEADERS);r.raise_for_status();return r.text

def listing(html):
    soup=BeautifulSoup(html,'html.parser'); found={}
    for tr in soup.select('tr'):
        cells=tr.find_all('td',recursive=False)
        if len(cells)<2:continue
        code=text(cells[0]); link=cells[1].find('a',href=True)
        if not re.fullmatch(r'\d{3,8}',code) or not link:continue
        url=urljoin(ROOT,link['href']); u=urlparse(url)
        if u.netloc.lower() not in ('www.acscourier.net','acscourier.net') or not u.path.startswith('/el/acs-lockers/') or u.path.rstrip('/')=='/el/acs-lockers':continue
        name=text(link)
        if not name:continue
        found[code]={'code':code,'name':name,'Country_Code':'GR','is_locker':True,'type':'locker','source_url':url,'address':'','city':'','postcode':'','venue_name':'','search_aliases':''}
    return found

def read_detail(row):
    """Extract visible address heading from ACS detail page, never assume postal codes."""
    html=get(row['source_url']);soup=BeautifulSoup(html,'html.parser')
    # Official ACS detail pages: h2 for title and h5 for venue/street/postcode.
    candidates=[]
    for selector in ('h5','.store-address','.address','[itemprop="streetAddress"]'):
        for element in soup.select(selector):
            v=text(element)
            if 6<=len(v)<=250 and re.search(r'\b\d{5}\b',v): candidates.append(v)
        if candidates:break
    if not candidates:
        # fall back only to visible text; avoid unrelated 5-digit IDs elsewhere.
        for element in soup.select('h3,h4,p'):
            v=text(element)
            if len(v)<170 and re.search(r'\b\d{5}\b',v) and (',' in v or re.search(r'\d+\s*,?\s*\d{5}',v)):
                candidates.append(v)
    if candidates:
        address=candidates[0];postcode=re.search(r'\b(\d{5})\b',address)
        row['postcode']=postcode.group(1) if postcode else ''
        row['address']=re.sub(r'[,\s]*\b\d{5}\b\s*$','',address).strip(' ,')
        # ACS sometimes prefixes the host business before the street address.
        match=re.search(r'^(.*?),\s*([^,]*\d[^,]*)$',row['address'])
        if match and not re.search(r'\d',match.group(1)):
            row['venue_name']=match.group(1).strip()
        row['address_source']=row['source_url']
    title=text(soup.find('h1') or soup.find('h2'))
    if title and len(title)<180 and 'Smartpoint' in title:row['name']=title
    return row

def rows_from_feed(data):
    if isinstance(data,list):return data
    if not isinstance(data,dict):return []
    for k in ('points','stations','data','result','Table_Data1'):
        if isinstance(data.get(k),list):return data[k]
    for key in ('ACSOutputResponse','ACSOutputResponce'):
        inner=data.get(key,{})
        if isinstance(inner,dict):
            table=inner.get('ACSTableOutput',{})
            if isinstance(table,dict):return table.get('Table_Data1',table.get('Table_Data',[])) or []
    return []

def pick(r,*names):
    for k in names:
        v=r.get(k)
        if v is not None and str(v).strip():return str(v).strip()
    return ''

def enrich_from_secondary(found):
    if not SECOND_URL:return 0
    if not SECOND_URL.startswith('https://'):raise ValueError('ACS_SECOND_SOURCE_URL must be HTTPS')
    r=requests.get(SECOND_URL,headers=HEADERS,timeout=50);r.raise_for_status();feed=r.json();used=0
    for other in rows_from_feed(feed):
        if not isinstance(other,dict):continue
        code=pick(other,'code','Code','ACS_SHOP_ID_CODE','ID','id')
        # Do not add unknown points: the extra ACS feed can contain non-locker branches.
        if code not in found:continue
        country=pick(other,'Country_Code','country_code','country','ACS_SHOP_COUNTRY_DESCR').upper()
        if country and country not in ('GR','GRC','GREECE','ΕΛΛΑΔΑ','1'):continue
        kind=pick(other,'ACS_SHOP_KIND','shop_kind','kind')
        flag=str(other.get('is_locker','')).lower()=='true'
        if kind and kind not in ('8','12'):continue
        if not kind and not flag and 'locker' not in pick(other,'type','Type').lower():
            # Same code may have generic metadata; allow enrichment but not classification.
            pass
        point=found[code]
        for dst,keys in {
            'address':['address','Address','ACS_SHOP_ADDRESS','Acs_Station_Address'],
            'city':['city','City','ACS_SHOP_AREA_DESCR','Acs_Station_City'],
            'postcode':['postcode','postal_code','ACS_SHOP_ZIPCODE','ZipCode','PostalCode'],
            'venue_name':['venue_name','store_name','shop_name','ACS_SHOP_NAME'],
            'search_aliases':['search_aliases','aliases']}.items():
            if not point.get(dst):
                value=pick(other,*keys)
                if value:point[dst]=value;used+=1
    return used

def apply_overrides(found):
    if not OVERRIDES.exists():return
    with OVERRIDES.open(encoding='utf-8-sig',newline='') as f:
        for item in csv.DictReader(f):
            row=found.get(str(item.get('code','')).strip())
            if not row:continue
            for k in ('address','city','postcode','search_aliases','venue_name'):
                if (item.get(k) or '').strip():row[k]=item[k].strip()

def main():
    found=listing(get(ROOT))
    old_count=0
    if OUT.exists():
        try:old_count=len(rows_from_feed(json.loads(OUT.read_text(encoding='utf-8'))))
        except (ValueError,TypeError):pass
    if len(found)<500 or (old_count>=500 and len(found)<old_count*0.85):
        raise RuntimeError(f'Found {len(found)} public directory entries (previous: {old_count}). Refusing to replace data.')
    errors=[]
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures={pool.submit(read_detail,row):code for code,row in found.items()}
        for f in as_completed(futures):
            try:f.result()
            except Exception as exc:errors.append((futures[f],str(exc)))
    if len(errors)>len(found)*0.25:
        raise RuntimeError(f'{len(errors)} detail pages failed; refusing incomplete update. Examples: {errors[:3]}')
    enriched=enrich_from_secondary(found)
    apply_overrides(found)
    records=sorted(found.values(),key=lambda r:int(r['code']))
    payload={'updated_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
             'source':ROOT,'secondary_source':SECOND_URL or None,
             'note':'ACS public directory; not live availability or shipping authorization',
             'count':len(records),'with_postcode':sum(bool(x['postcode']) for x in records),
             'with_address':sum(bool(x['address']) for x in records),
             'detail_page_failures':len(errors),'secondary_fields_added':enriched,'points':records}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Saved',len(records),'ACS lockers;',payload['with_postcode'],'postcodes;',payload['with_address'],'addresses; secondary fields:',enriched)
if __name__=='__main__':main()
