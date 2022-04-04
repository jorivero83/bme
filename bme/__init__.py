import re
import time
from tqdm import tqdm
import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bme.constants import IBEX_URL


__all__ = ['BME', 'get_date', 'get_meta', 'IBEX_URL']


class BME:

    def __init__(self, url=None, data_dir=None):
        self.soup = BeautifulSoup(urlopen(url=url or IBEX_URL), features="lxml")
        self.data_dir = data_dir   # todo: add source root

    def get_index_table(self):
        tbl = self.soup.find('table', attrs={'id': 'ctl00_Contenido_tblÍndice'})
        tbl_values, cols = [], []
        for i, tr in enumerate(tbl.find_all('tr')):
            if i == 0:
                cols = [v.text for v in tr.find_all('th')]
            else:
                tbl_values.append([v.text for v in tr.find_all('td')])
        return pd.DataFrame(data=tbl_values, columns=cols)

    def get_underlyings_table(self):
        tbl = self.soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
        tbl_values, cols = [], []
        for i, tr in enumerate(tbl.find_all('tr')):
            if i == 0:
                cols = [v.text for v in tr.find_all('th')]
            else:
                tbl_values.append([v.text for v in tr.find_all('td')])
        return pd.DataFrame(data=tbl_values, columns=cols)

    def get_underlyings_urls(self):
        map_urls = {}
        tbl = self.soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
        for a in ['DifFlSb', 'DifFlBj']:
            for v in tbl.find_all('td', attrs={'class': a}):
                # print(v.text, 'https://www.bolsamadrid.es' + v.a.get('href'))
                map_urls[v.text] = 'https://www.bolsamadrid.es' + str(v.a.get('href'))

        return map_urls

    def get_underlying_history_data(self, url):
        soup = BeautifulSoup(urlopen(url=url), features="lxml")
        tbl_obj = soup.find_all('table', attrs={'class': 'TblPort', 'id': "ctl00_Contenido_tblDatos"})[0]
        tbl_values, cols = [], []
        for i, tr in enumerate(tbl_obj.find_all('tr')):
            if i == 0:
                cols = [v.text for v in tr.find_all('th')]
            else:
                tbl_values.append([a.text for a in tr.find_all('td')])

        return pd.DataFrame(data=tbl_values, columns=cols)

    def get_underlyings_history_data(self):
        map_urls = self.get_underlyings_urls()
        n_urls = len(list(map_urls))
        dfs = []
        for v in tqdm(map_urls, desc='Downloading history data', total=n_urls):
            url = str(map_urls[v]).replace('FichaValor', 'InfHistorica')
            tmp = self.get_underlying_history_data(url)
            tmp_meta = get_meta(url)
            tmp['isin'] = tmp_meta['ISIN']
            tmp['symbol'] = tmp_meta['Ticker']
            tmp['company'] = v
            tmp['url_of_data'] = url
            tmp['Desde'] = tmp_meta['Desde']
            tmp['Hasta'] = tmp_meta['Hasta']
            dfs.append(tmp)
            time.sleep(10)

        return pd.concat(dfs, ignore_index=True)


def get_date(obj):
    date_str = ''
    if obj.find('input', attrs={'id': 'ctl00_Contenido_Desde_Dia'}):
        day = obj.find('input', attrs={'id': 'ctl00_Contenido_Desde_Dia'}).attrs['value']
        month = obj.find('input', attrs={'id': 'ctl00_Contenido_Desde_Mes'}).attrs['value']
        year = obj.find('input', attrs={'id': 'ctl00_Contenido_Desde_Año'}).attrs['value']
        date_str = year + '-' + month + '-' + day
    if obj.find('input', attrs={'id': 'ctl00_Contenido_Hasta_Dia'}):
        day = obj.find('input', attrs={'id': 'ctl00_Contenido_Hasta_Dia'}).attrs['value']
        month = obj.find('input', attrs={'id': 'ctl00_Contenido_Hasta_Mes'}).attrs['value']
        year = obj.find('input', attrs={'id': 'ctl00_Contenido_Hasta_Año'}).attrs['value']
        date_str = year + '-' + month + '-' + day
    return date_str


def get_meta(x):
    soup_str = BeautifulSoup(urlopen(url=x), features="lxml")
    table = soup_str.find('table', attrs={'class': "FrmBusq"})
    table_vals, table_headers = [], []
    cols = [v.text for v in table.find_all('td', attrs={'class': 'Etiqueta2'})]
    # print([v.text for v in table.find_all('td', attrs={'class': 'Etiqueta2'})])
    row = []
    for td in table.find_all('td', attrs={'class': 'Campo'}):
        if td.find('input'):
            val = get_date(td)
        else:
            val = re.sub('^\s+|\s+$', '', td.text)
        # print(val)
        row.append(val)
    table_vals.append(row)
    return pd.DataFrame(data=table_vals, columns=cols).iloc[-1].to_dict()


if __name__ == '__main__':
    from pprint import pprint
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    sp = BME()
    print(sp.get_index_table())
    # print(sp.get_underlyings_table())
    # pprint(sp.get_underlyings_urls())
    # print(sp.get_underlyings_history_data())


