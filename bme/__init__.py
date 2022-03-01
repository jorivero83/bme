import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import pandas as pd
from bme.constants import IBEX_URL, IBEX_COMPANIES, COLS_TABLE_INDEX, COLS_TABLE_UNDERLYINGS
from tqdm import tqdm
import time

# class BME:
#
#     def __init__(self, data_dir=None):
#         self.soup_ibex = BeautifulSoup(urlopen(url=IBEX_URL))
#         self.data_dir = data_dir   # todo: add source root
#
#     def get_intraday_data(self, url):
#         soup = BeautifulSoup(urlopen(url=url), features="lxml")
#         table_index, table_underlyings = [], []
#         for tr in soup.find_all('tr'):
#             tds = tr.find_all('td')
#             if len(tds) == 0:
#                 continue
#             print(tds[0].text)
#             if tds[0].text == 'IBEX 35®':
#                 table_index.append([a.text for a in tds])
#             elif tds[0].text in IBEX_COMPANIES:
#                 table_underlyings.append([a.text for a in tds])
#             else:
#                 pass
#         df_index = pd.DataFrame(data=table_index, columns=COLS_TABLE_INDEX)
#         df_underlyings = pd.DataFrame(data=table_underlyings, columns=COLS_TABLE_UNDERLYINGS)
#         return df_index, df_underlyings
#
#     def get_security_meta_data(self):
#         table_form = soup2.find('table', attrs={'class': "FrmBusq"})
#         table_form_vals, table_form_headers = [], []
#         for i, tr in enumerate(table_form.find_all('tr')):
#             if i == 0:
#                 firs_obj = tr.find('td', attrs={'class': 'Etiqueta2'})
#                 if firs_obj is not None:
#                     print([firs_obj.text] + [v.text for v in firs_obj.find_next_siblings('td')])
#                     table_form_headers = [firs_obj.text] + [v.text for v in firs_obj.find_next_siblings('td')]
#             else:
#                 tds = tr.find_all('td')
#                 if len(tds) == len(table_form_headers):  # [re.sub('^\s+|\s+$','',v) for v in obj_list]
#                     vals = []
#                     for td in tds:
#                         if td.find('input'):
#                             val = get_date(td)
#                         else:
#                             val = re.sub('^\s+|\s+$', '', td.text)
#                         print(val)
#                         vals.append(val)
#                     table_form_vals.append(vals)
#
#             df_table_form = pd.DataFrame(data=table_form_vals, columns=table_form_headers)
#
#             return df_table_form.iloc[0].to_dict()


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


class IbexSessionPrices:

    def __init__(self, url, data_dir=None):
        self.soup = BeautifulSoup(urlopen(url=url), features="lxml")
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
        # tbl = self.soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
        # map_urls = {}
        # for tr in tbl.find_all('tr'):
        #     for v in tr.find_all('td', attrs={'class': 'DifFlSb'}):
        #         if v.a is not None:
        #             map_urls[v.text] = 'https://www.bolsamadrid.es' + str(v.a.get('href'))
        tbl = self.soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
        map_urls = {}
        for v in tbl.find_all('td', attrs={'class': 'DifFlSb'}):
            print(v.text, 'https://www.bolsamadrid.es' + v.a.get('href'))
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

    sp = IbexSessionPrices(url=IBEX_URL)
    # print(sp.get_index_table())
    print(sp.get_underlyings_table())
    # print(sp.get_underlyings_history_data())
    # pprint(sp.get_underlyings_urls())

