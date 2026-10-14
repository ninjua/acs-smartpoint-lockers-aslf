#!/usr/bin/env python3
"""ACS public directory export. Not live availability or shipment routing authorization."""
import csv
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

ROOT = 'https://www.acscourier.net/el/acs-lockers/'
OUT = Path(__file__).with_name('acs-lockers.json')
OVERRIDES = Path(__file__).with_name('acs-locker-overrides.csv')
HEADERS = {'User-Agent': 'Mozilla/5.0 (compatible; merchant-directory-sync/1.1)'}

def parse_directory(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = {}
    # Use the actual table cells; don't reject records that don't say "smartpoint".
    for tr in soup.select('tr'):
        cells = tr.find_all('td', recursive=False)
        if len(cells) < 2:
            continue
        code = cells[0].get_text(' ',strip=True)
        if not re.fullmatch(r'\d{3,8}', code):
            continue
        link = cells[1].find('a',href=True)
        if not link:
            continue
        url = urljoin(ROOT,link['href'])
        u = urlparse(url)
        if u.netloc.lower() not in ('www.acscourier.net','acscourier.net') or '/el/acs-lockers/' not in u.path or u.path.rstrip('/') == '/el/acs-lockers':
            continue
        name = re.sub(r'\s+',' ',link.get_text(' ',strip=True)).strip()
        if not name:
            continue
        rows[code] = {'code':code,'name':name,'Country_Code':'GR','is_locker':True,
                      'type':'locker','source_url':url,'address':'','city':'','postcode':'',
                      'search_aliases':''}
    return sorted(rows.values(),key=lambda r:int(r['code']))

def overlay(records):
    """Optional verified merchant data; postcode/city must not be invented."""
    if not OVERRIDES.exists():
        return records
    idx = {r['code']:r for r in records}
    with OVERRIDES.open(encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            code = str(row.get('code','')).strip()
            if code not in idx:
                continue
            for key in ('address','city','postcode','search_aliases','venue_name'):
                if row.get(key, '').strip():
                    idx[code][key] = row[key].strip()
    return records

def main():
    r = requests.get(ROOT,headers=HEADERS,timeout=45)
    r.raise_for_status()
    records = overlay(parse_directory(r.text))
    old_count = 0
    if OUT.exists():
        try: old_count=len(json.loads(OUT.read_text(encoding='utf-8')).get('points',[]))
        except (ValueError,TypeError): pass
    # Safety rails: fail if parser breaks or directory suddenly shrinks drastically.
    if len(records)<500 or (old_count >= 500 and len(records) < old_count * 0.85):
        raise RuntimeError(f'Found only {len(records)} lockers (previous: {old_count}); not overwriting. Check directory HTML.')
    payload = {'updated_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
               'source':ROOT,'note':'ACS published directory, NOT real-time locker availability',
               'count':len(records),'points':records}
    OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Parsed:',len(records),'previous:',old_count,'saved:',OUT)

if __name__=='__main__': main()
