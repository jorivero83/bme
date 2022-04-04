from urllib.request import urlopen
import certifi
import json
import pandas as pd
import os
from collections import OrderedDict
from tqdm import tqdm
from datetime import (date, datetime)
import yahoo_fin.stock_info as si
import joblib
from bs4 import BeautifulSoup
from bme import get_meta

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

get_meta("https://www.bolsamadrid.es/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0125220311")

url = "https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
soup = BeautifulSoup(urlopen(url=url), features="lxml")

soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})

aux = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
for a in ['DifFlSb', 'DifFlBj']:
    for v in aux.find_all('td', attrs={'class': a}):
        print(v.text, 'https://www.bolsamadrid.es' +v.a.get('href'))

for v in aux.find_all('td', attrs={'class': 'DifFlBj'}):
    print(v.text, 'https://www.bolsamadrid.es' +v.a.get('href'))

for tr in aux.find_all('tr'):
    print([td.text for td in tr.find_all('td')])

map_urls = {}
aux = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
for a in ['DifFlSb', 'DifFlBj']:
    for v in aux.find_all('td', attrs={'class': a}):
        print(v.text, 'https://www.bolsamadrid.es' +v.a.get('href'))
        map_urls[v.text] = 'https://www.bolsamadrid.es' + str(v.a.get('href'))
