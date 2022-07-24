import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def collect_inmates():
    response = requests.get(
        'https://gtlinterface.bernco.gov/custodylist/Results')

    soup = bs(response.text, 'html.parser')

    tables = soup.find_all('table')

    table_rows = tables[0].find_all('tr')

    inmates = {}

    for row in table_rows:
        td = row.find_all('td')
        if len(td) > 0:
            inmate_info = td[3].find_all('a')
            inmate_id = inmate_info[0].text.strip()
            inmate_link = inmate_info[0]['href'].strip()
            inmates[inmate_id] = inmate_link

    return inmates
