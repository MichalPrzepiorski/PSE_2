#Ubytki mocy JWCD cieplnych
#Zapotrzebowanie mocy KSE
#Generacja mocy jednostek wytwórczych
#Generacja źródeł wiatrowych i fotowoltaicznych
#Przepływy mocy na poszczególnych przekrojach handlowych
#Wielkości podstawowe
#Bilans mocy w szczycie rannym i wieczornym
#Kompensowanie niezbilansowań
from Ubytki_mocy_JWCD_cieplnych import Jeden 
from Zapotrzebowanie_mocy_KSE import Dwa 
from Generacja_mocy_jednostek_wytworczych import Trzy
from Generacja_zrodel_wiatrowych_i_fotowoltaicznych import Cztery
from Przepływy_mocy_na_poszczegolnych_przekrojach_handlowych import Pięć
from Wielkosci_podstawowe import Sześć
from Bilans_mocy_w_szczycie_rannym_i_porannym import Siedem
from Kompensowanie_niezbilansowan import Osiem

class Wybor_zagadnienia:    
    def Wybor_zagadnienia():
        print("""
        1-Ubytki mocy JWCD cieplnych
        2-Zapotrzebowanie mocy KSE
        3-Generacja mocy jednostek wytwórczych
        4-Generacja źródeł wiatrowych i fotowoltaicznych
        5-Przepływy mocy na poszczególnych przekrojach handlowych
        6-Wielkości podstawowe
        7-Bilans mocy w szczycie rannym i wieczornym
        8-Kompensowanie niezbilansowań inne""")
        Zagadnienie=input('Podaj odpowiednią liczbę, aby pobrać odpowiednie pliki\n-->')

        if Zagadnienie == '1':
            Nazwy = Jeden.Jeden()
        elif Zagadnienie == '2':
            Nazwy = Dwa.Dwa()
        elif Zagadnienie == '3':
             Nazwy =Trzy.Trzy()
        elif Zagadnienie == '4':
            Nazwy = Cztery.Cztery()
        elif Zagadnienie == '5':
            Nazwy = Pięć.Pięć()
        elif Zagadnienie == '6':
            Nazwy = Sześć.Sześć()
        elif Zagadnienie == '7':
            Nazwy = Siedem.Siedem()
        elif Zagadnienie == '8':
            Nazwy = Osiem.Osiem()
        else:
            print('Zły numer!')

        return(Nazwy)


