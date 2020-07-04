#! python3

# Box-office scraper

import requests

def url_to_file(url, filename='world.html'):
    r = requests.get(url)
    if r.status_code == 200:
        hmtl_text = r.text

url='https://www.boxofficemojo.com/year/world/'


print(r.status_code)