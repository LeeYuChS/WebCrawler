import ssl
import certifi
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

context = ssl.create_default_context(cafile=certifi.where())
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36'
}

def fetch_data(url, column_name, convert_numeric=False):
    """爬取 IndexMundi 資料並回傳 DataFrame"""
    req = Request(url, headers=HEADERS)
    html = urlopen(req, context=context).read().decode('utf-8', errors='ignore')
    soup = BeautifulSoup(html, 'html.parser')

    table = soup.find('table', {'class': 'data-table'})
    if table is None:
        raise ValueError(f"Table not found for URL: {url}")

    rows = table.find_all('tr')
    years = [th.text.strip() for th in rows[0].find_all('th')[1:]]
    values = [td.text.strip() for td in rows[1].find_all('td')[1:]]

    if convert_numeric:
        values = [int(v.replace(',', '')) if v.replace(',', '').isdigit() else None for v in values]
    else:
        values = [float(v.replace(',', '')) if v.replace(',', '').replace('.', '').isdigit() else None for v in values]

    data = dict(zip(years, values))
    df = pd.DataFrame.from_dict(data, orient='index', columns=[column_name])
    return df

