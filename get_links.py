# Date : Dec 15th 2024
# Purpose: WebScraper
# Authors: Wil
# Date Updated: Dec 15th 2024

import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.1',
}

response = requests.get(
    'https://regrodeo.com/api/regulations?&year=2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024',
    headers=headers,
)

data = response.json()
url_base = "https://regrodeo.com/api/regulation/"

output = []

for i,entry in enumerate(data):
    url = url_base + f"{entry['name']}--{entry['year']}--{entry['total_cost']}"
    datum = requests.get(url).json()
    output.append(datum)
    #if i > 10: break

df = pd.DataFrame(output)
df.to_csv("sample.csv", index=False)
