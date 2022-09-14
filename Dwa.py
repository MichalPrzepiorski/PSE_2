from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import glob
import sys
from Dni_miesiaca import Date
import time

class Dwa:
    def Dwa():
        Rokpoczatkowy=input('Podaj poczatkowy rok\n-->')
        Miesiacpoczatkowy=input('Podaj poczatkowy miesiac\n-->')
        Dzienpoczatkowy=input('Podaj poczatkowy dzien\n-->')
        Rokkoncowy=input('Podaj koncowy rok\n-->')
        Miesiackoncowy=input('Podaj koncowy miesiac\n-->')
        Dzienkoncowy=input('Podaj koncowy dzien\n-->')
        Slownik = Date(Rokpoczatkowy, Rokkoncowy, Miesiacpoczatkowy, Miesiackoncowy, Dzienpoczatkowy, Dzienkoncowy)
        Lista=Slownik.Przygotowanie_danych()
        zmienna = Dwa.Dwa2(Lista)
        return(zmienna)

    def Dwa2(Lista):
        data = Lista
        print(data)
        Nazwy=[]
        lista=list(zip(data, data[1:]))[::2]
        print(lista)
        cd = os.getcwd()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", cd)
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
        path_gecko = '{}\geckodriver-v0.31.0-win64\geckodriver.exe'.format(cd)
        web = webdriver.Firefox(firefox_profile=profile, executable_path=path_gecko)
        web.get("https://www.pse.pl/dane-systemowe/funkcjonowanie-kse/raporty-dobowe-z-pracy-kse/zapotrzebowanie-mocy-kse")
        time.sleep(3)

        # try:
        for daty1 in lista:
            time.sleep(10)
            data_poczatkowa = daty1[0][:4] + '-' + daty1[0][4:6] + '-' + daty1[0][6:]
            data_koncowa = daty1[1][:4] + '-' + daty1[1][4:6] + '-' + daty1[1][6:]
            print(data_poczatkowa)
            print(data_koncowa)
            poczatek = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_fromDate"]').clear()
            poczatek = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_fromDate"]')
            poczatek.send_keys(data_poczatkowa)
            koniec = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_toDate"]').clear()
            koniec = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_toDate"]') 
            koniec.send_keys(data_koncowa)
            pobierz = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_csvPeriod"]') 
            pobierz.click()
            f = True
            while f:
                try:
                    path_download = '{}/ZAP_KSE*.*'.format(cd)
                    f = False
                except:
                    continue
              
            path_download = '{}/ZAP_KSE*.*'.format(cd)
            name_download = glob.glob(path_download)[0]
            print(name_download)
            nazwa_pliku = '{}-{}'.format(daty1[0], daty1[1])
            path_save = '{}/{}.csv'.format(glob.glob(cd)[0], nazwa_pliku)
            os.rename(name_download, path_save)
            Nazwy.append('{nazwa_pliku1}.csv'.format(nazwa_pliku1 = nazwa_pliku))
        web.close()

        # except:
            # print('Najprawdopdobniej błąd strony\nPrawdopodobnie zostaly wpisane daty ktorych strona nie obsluguje')
            # sys.exit()


        return(Nazwy)
