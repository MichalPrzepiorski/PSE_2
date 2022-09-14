import urllib.request
import sys
from Dni_miesiaca import Date

class Osiem:
    def Osiem(Lista):
        data = Lista
        Nazwy=[]
        try:

            lista=list(zip(data, data[1:]))[::2]

            for daty1 in lista:
                nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                url='https://www.pse.pl/getcsv/-/export/csv/PL_IMBALANCE_NETTING/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                urllib.request.urlretrieve(url, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                
            return(Nazwy, lista)

        except:

            print('Najprawdopdobniej błąd strony\nPrawdopodobnie zostaly wpisane daty ktorych strona nie obsluguje')
            sys.exit()