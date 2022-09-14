import urllib.request
import sys
from Dni_miesiaca import Date

#Ubytki mocy JWCD cieplnych

class Jeden:
    def Jeden():
        Rokpoczatkowy=input('Podaj poczatkowy rok\n-->')
        Miesiacpoczatkowy=input('Podaj poczatkowy miesiac\n-->')
        Dzienpoczatkowy=input('Podaj poczatkowy dzien\n-->')
        Rokkoncowy=input('Podaj koncowy rok\n-->')
        Miesiackoncowy=input('Podaj koncowy miesiac\n-->')
        Dzienkoncowy=input('Podaj koncowy dzien\n-->')
        Slownik = Date(Rokpoczatkowy, Rokkoncowy, Miesiacpoczatkowy, Miesiackoncowy, Dzienpoczatkowy, Dzienkoncowy)
        Lista=Slownik.Przygotowanie_danych()
        zmienna = Jeden.Jeden1(Lista)
        return(zmienna)

    def Jeden1(Lista):
        data = Lista
        Nazwy=[]
        try:

            lista=list(zip(data, data[1:]))[::2]

            for daty1 in lista:
                nazwa_pliku = '{poczatek}-{koniec}'.format(poczatek = daty1[0], koniec = daty1[1])
                Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                url='https://www.pse.pl/getcsv/-/export/csv/PL_WYK_UBYTKI/data_od/{z}/data_do/{k}'.format(z = daty1[0], k = daty1[1])
                #urllib.request.urlretrieve(url, '{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
                
            return(Nazwy)

        except:

            print('Najprawdopdobniej błąd strony\nPrawdopodobnie zostaly wpisane daty ktorych strona nie obsluguje')
            sys.exit()