from selenium import webdriver
from selenium.webdriver.common.by import By
from shutil import move
import os
import glob
import time

pierwsza = input('Podaj_date1')
druga = input('Podaj_date_2')
cd = os.getcwd()
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", cd)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

path_gecko = '{}\geckodriver-v0.31.0-win64\geckodriver.exe'.format(cd)
web = webdriver.Firefox(firefox_profile=profile, executable_path=path_gecko)
web.get("https://www.pse.pl/dane-systemowe/funkcjonowanie-kse/raporty-dobowe-z-pracy-kse/zapotrzebowanie-mocy-kse")

time.sleep(10)
poczatek = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_fromDate"]').clear()
poczatek = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_fromDate"]')
poczatek.send_keys(pierwsza)
koniec = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_toDate"]').clear()
koniec = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_toDate"]') 
koniec.send_keys(druga)
time.sleep(5)
pobierz = web.find_element(By.XPATH, '//*[@id="_danekse_WAR_danekserbportlet_csvPeriod"]') 
pobierz.click()



web.close()


# path_download = '{}\ZAP_KSE*.*'.format(cd)
# name_download = glob.glob(path_download)[0]
# path_save = '{}\\plik.csv'.format(glob.glob(cd)[0])
# print(path_save)
# move(name_download, path_save)
#"C:\Users\mprze\Desktop\PSE (2)\ZAP_KSE_20220101to20220105_20220111130529.csv"