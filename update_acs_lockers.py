#!/usr/bin/env python3
"""Create Shopify-compatible locker JSON from the PUBLIC ACS lockers directory.
Directory publication is NOT confirmation of live locker availability.
"""
import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

URL = 'https://www.acscourier.net/el/acs-lockers/'
OUT = Path(__file__).with_name('acs-lockers.json')
HEADERS = {'User-Agent': 'ACS-Locker-Directory-Exporter/1.0 (merchant inventory sync)'}

def parse_directory(html):
    soup = BeautifulSoup(html, 'html.parser')
    found = {}
    # Directory presents a numbered HTML table with detail-page links.
    for row in soup.select('tr'):
        cells = row.find_all(['td', 'th'], recursive=False)
        if len(cells) < 2:
            continue
        code = cells[0].get_text(' ', strip=True)
        a = cells[1].find('a', href=True)
        if not re.fullmatch(r'\d{3,8}', code) or not a:
            continue
        name = re.sub(r'\s+', ' ', a.get_text(' ', strip=True)).strip()
        if not re.search(r'(?:smart\s*point|smartpoint|locker)', name, re.I):
            continue
        href = urljoin(URL, a['href'])
        if not href.startswith('https://www.acscourier.net/el/acs-lockers/'):
            continue
        found[code] = {
            'code': code,
            'name': name,
            'Country_Code': 'GR',
            'is_locker': True,
            'type': 'locker',
            'source_url': href,
            # Directory index does not consistently publish these fields.
            'address': '',
            'city': '',
            'postcode': '',
        }
    return sorted(found.values(), key=lambda item: int(item['code']))

def main():
    response = requests.get(URL, headers=HEADERS, timeout=35)
    response.raise_for_status()
    records = parse_directory(response.text)
    if len(records) < 100:
        raise RuntimeError(f'Only {len(records)} lockers parsed; refusing to overwrite existing feed')
    data = {'updated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
            'source': URL, 'note': 'Public ACS directory, not real-time availability',
            'points': records}
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Saved {len(records)} unique directory locker entries to {OUT}')

if __name__ == '__main__':
    main()
