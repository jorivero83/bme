# BME
A package to download data from [www.bolsamadrid.es](https://www.bolsamadrid.es/)

## Getting started ##

### Install 

```commandline
pip install git+https://github.com/jorivero83/bme.git
```

### Basic usage ###

Import the package and ibex url
```commandline
>> from bme import BME
```

Getting index table
```commandline
>> BME().get_index_table()
```
```commandline
     Nombre  Anterior    Último % Dif.    Máximo    Mínimo       Fecha      Hora % Dif.Año 2022
0  IBEX 35®  8.503,70  8.481,60  -0,26  8.546,40  8.443,70  04/04/2022  11:14:54          -2,66
```

Getting session prices of underlyings of IBEX35
```commandline
>> BME().get_underlyings_table()
```
```commandline
          Nombre      Últ. % Dif.      Máx.      Mín.     Volumen Efectivo (miles €)       Fecha      Hora
0        ACCIONA  176,4000   0,34  178,1000  175,9000      20.573           3.644,29  04/04/2022  11:16:00
1       ACERINOX    9,9720  -1,71   10,1550    9,8680     611.156           6.074,15  04/04/2022  11:16:41
2            ACS   24,4300  -0,65   24,7700   24,3700     138.585           3.402,30  04/04/2022  11:15:28
3           AENA  143,5500  -2,45  147,6000  143,1000      29.722           4.309,08  04/04/2022  11:15:15
4       ALMIRALL   11,6500   1,39   11,6800   11,5500      67.197             780,85  04/04/2022  11:16:34
5        AMADEUS   58,4200  -0,07   58,9200   57,8800     660.796          38.594,92  04/04/2022  11:17:02
6    ARCELORMIT.   29,6600  -0,37   29,7300   29,2700      98.508           2.904,07  04/04/2022  11:15:19
7    B.SANTANDER    3,1860   0,16    3,1980    3,1490   8.510.446          26.990,91  04/04/2022  11:17:03
8    BA.SABADELL    0,7486  -0,37    0,7570    0,7388   8.001.838           5.956,65  04/04/2022  11:16:55
9      BANKINTER    5,3960   0,19    5,4000    5,3300     334.520           1.793,42  04/04/2022  11:17:04
10          BBVA    5,2800  -0,19    5,3430    5,2290  68.862.115         361.721,77  04/04/2022  11:17:01
11     CAIXABANK    3,1560  -0,57    3,1910    3,1240   6.635.238          21.013,10  04/04/2022  11:17:03
12       CELLNEX   43,9800  -0,09   44,3700   43,9200     103.761           4.571,17  04/04/2022  11:16:50
13  CIE AUTOMOT.   20,5000   0,00   20,6200   20,2600      54.446           1.110,75  04/04/2022  11:14:18
14        ENAGAS   20,2400   0,15   20,3300   20,1500     100.513           2.035,70  04/04/2022  11:16:49
15        ENDESA   19,3650  -1,32   19,7550   19,3650     161.726           3.159,17  04/04/2022  11:16:42
16     FERROVIAL   24,2300  -0,62   24,5300   24,1700     109.446           2.658,23  04/04/2022  11:16:12
17       FLUIDRA   25,1800  -0,08   25,5400   24,8800      95.217           2.391,04  04/04/2022  11:14:50
18  GRIFOLS CL.A   16,8800   2,52   16,9100   16,6400     300.446           5.046,01  04/04/2022  11:16:01
19           IAG    1,6570  -1,49    1,7035    1,6510   6.552.995          10.908,53  04/04/2022  11:16:57
20     IBERDROLA    9,9480   0,34   10,0050    9,9100   1.167.700          11.627,82  04/04/2022  11:17:02
21       INDITEX   19,7350  -1,86   20,1300   19,4300   2.020.884          39.793,28  04/04/2022  11:17:02
22       INDRA A    9,5400   0,42    9,7300    9,5300     275.561           2.647,20  04/04/2022  11:16:30
23  INM.COLONIAL    8,2850   0,30    8,3350    8,2350     107.550             889,72  04/04/2022  11:15:43
24        MAPFRE    1,9090   0,10    1,9160    1,8980     546.562           1.041,01  04/04/2022  11:11:40
25  MELIA HOTELS    6,5800  -2,23    6,8300    6,5700     183.422           1.218,46  04/04/2022  11:16:27
26        MERLIN   10,9100   2,73   11,1100   10,7700     564.133           6.155,26  04/04/2022  11:16:38
27       NATURGY   26,8000  -0,22   27,0500   26,7300      40.104           1.076,72  04/04/2022  11:16:40
28    PHARMA MAR   72,7800   1,31   72,8000   71,0000      28.371           2.045,28  04/04/2022  11:16:38
29        R.E.C.   18,7800  -0,08   18,9850   18,7550     173.808           3.281,90  04/04/2022  11:14:40
30        REPSOL   11,9350  -0,08   12,0650   11,9000   1.865.789          22.374,24  04/04/2022  11:16:53
31          ROVI   67,2500   2,13   67,3000   66,0000       9.549             637,21  04/04/2022  11:16:02
32  SIEMENS GAME   15,8000  -0,91   16,3500   15,7400     363.831           5.835,23  04/04/2022  11:16:26
33       SOLARIA   20,4700  -1,44   21,5500   20,3200     353.093           7.412,79  04/04/2022  11:16:59
34    TELEFONICA    4,3900  -0,61    4,4280    4,3800   1.782.211           7.832,59  04/04/2022  11:17:03
```


Getting historical data for last month of 35 assets of IBEX35.
```commandline
>> BME().get_underlyings_history_data()
```

```commandline
Downloading history data: 100%|██████████| 35/35 [06:02<00:00, 10.36s/it]
          Fecha    Cierre Referencia     Volumen       Efectivo    Último    Máximo    Mínimo     Medio          isin symbol     company                                        url_of_data       Desde       Hasta
0    04/03/2022  139,3000   141,3000     133.579  18.624.919,20  139,3000  143,2000  137,9000  139,4310  ES0125220311    ANA     ACCIONA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
1    07/03/2022  145,9000   139,3000     156.993  22.574.183,50  145,9000  147,8000  135,2000  143,7910  ES0125220311    ANA     ACCIONA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
2    08/03/2022  150,0000   145,9000     167.594  25.358.131,80  150,0000  154,0000  143,2000  151,3069  ES0125220311    ANA     ACCIONA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
3    09/03/2022  156,1000   150,0000     192.222  29.865.058,90  156,1000  157,2000  151,1000  155,3675  ES0125220311    ANA     ACCIONA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
4    10/03/2022  155,2000   156,1000     124.055  19.334.297,70  155,2000  159,3000  153,9000  155,8526  ES0125220311    ANA     ACCIONA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
..          ...       ...        ...         ...            ...       ...       ...       ...       ...           ...    ...         ...                                                ...         ...         ...
730  28/03/2022    4,3140     4,2395  14.229.721  61.581.651,21    4,3140    4,3830    4,2425    4,3317  ES0178430E18    TEF  TELEFONICA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
731  29/03/2022    4,3560     4,3140  15.124.860  66.068.652,64    4,3560    4,4105    4,3150    4,3682  ES0178430E18    TEF  TELEFONICA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
732  30/03/2022    4,4120     4,3560  10.565.189  46.418.375,42    4,4120    4,4120    4,3415    4,3935  ES0178430E18    TEF  TELEFONICA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
733  31/03/2022    4,3885     4,4120  12.829.772  56.338.864,04    4,3885    4,4325    4,3580    4,3917  ES0178430E18    TEF  TELEFONICA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
734  01/04/2022    4,4170     4,3885   9.798.232  43.155.322,09    4,4170    4,4240    4,3670    4,4047  ES0178430E18    TEF  TELEFONICA  https://www.bolsamadrid.es/esp/aspx/Empresas/I...  2022-03-04  2022-04-03
```
