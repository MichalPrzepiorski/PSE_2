from calendar import monthrange
import sys
class Date:

    def __init__(self, danarx, danary, danamx, danamy, danadx, danady):
        self.danarx=int(danarx)
        self.danary=int(danary)
        self.danamx=int(danamx)
        self.danamy=int(danamy)
        self.danadx=int(danadx)
        self.danady=int(danady)
        
    def Przygotowanie_danych(self):    
        LATAL = []
        LATAD = {}
        Miesiace = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        #Lista z datami
        for rok in range(self.danary-self.danarx+1):
            LATAL.append(self.danarx+rok)

        #Przypisanie miesiecy do kazdego roku
        for LATA in LATAL:
            LATAD[LATA] = Miesiace


        #Przerobienie pierwszego i ostatniego roku na odpowiednia ilosc miesiecy
        Miesiace_rok_poczatkowy=Miesiace[(self.danamx-1):]
        Miesiace_rok_koncowy=Miesiace[:self.danamy]
        if self.danarx == self.danary:
            LATAD[self.danarx] = Miesiace[(self.danamx-1):self.danamy]
        else:
            LATAD[self.danarx] = Miesiace_rok_poczatkowy
            LATAD[self.danary] = Miesiace_rok_koncowy

        #Stworzenie listy ktora dla kazdego miesiaca przyporzadkowuje ilosc dni
        daty = []
        for key in LATAD:
            for miesiace in LATAD[key]:
                daty.append([key, miesiace, monthrange(key, miesiace)[1]])

        #Tworzenie dat i zapisywanie ich do listy
        #Zapisywanie poczatkowych dat
        daty3 = []

        if len(daty) == 1:
            print('Mozna pobrac recznie dokument z jednego miesiaca')
            sys.exit()
        else:
            if self.danadx != daty[0][2]:
                if len(str(self.danamx)) == 1:
                    if len(str(self.danadx)) == 1:
                        daty3.append("{}0{}0{}".format(self.danarx, self.danamx, self.danadx))
                        daty3.append("{}0{}{}".format(self.danarx, self.danamx, daty[0][2]))
                    else:
                        daty3.append("{}0{}{}".format(self.danarx, self.danamx, self.danadx))
                        daty3.append("{}0{}{}".format(self.danarx, self.danamx, daty[0][2]))
                else:
                    if len(str(self.danadx)) == 1:
                        daty3.append("{}{}0{}".format(self.danarx, self.danamx, self.danadx))
                        daty3.append("{}{}0{}".format(self.danarx, self.danamx, daty[0][2]))
                    else:
                        daty3.append("{}{}{}".format(self.danarx, self.danamx, self.danadx))
                        daty3.append("{}{}{}".format(self.danarx, self.danamx, daty[0][2]))
            else:
                if len(str(self.danamy)) == 1:
                    
                    daty3.append("{}0{}{}".format(self.danarx, self.danamx, self.danadx))

                else:

                    daty3.append("{}{}{}".format(self.danarx, self.danamx, self.danadx))

            #Zapisywanie dat "srodkowych"
            daty2 = daty[1:-1]
            for wartosci in daty2:
                if len(str(wartosci[1])) == 1:
                    if len(str(wartosci[2])) == 1:
                        daty3.append("{}0{}01".format(wartosci[0], wartosci[1]))
                        daty3.append("{}0{}0{}".format(wartosci[0], wartosci[1], wartosci[2]))
                    else:
                        daty3.append("{}0{}01".format(wartosci[0], wartosci[1]))
                        daty3.append("{}0{}{}".format(wartosci[0], wartosci[1], wartosci[2]))
                else:
                    if len(str(wartosci[2])) == 1:
                        daty3.append("{}{}01".format(wartosci[0], wartosci[1]))
                        daty3.append("{}{}0{}".format(wartosci[0], wartosci[1], wartosci[2]))
                    else:
                        daty3.append("{}{}01".format(wartosci[0], wartosci[1]))
                        daty3.append("{}{}{}".format(wartosci[0], wartosci[1], wartosci[2]))

            #Zapisywanie dat koncowych
            if self.danady != 1:
                if len(str(self.danamy)) == 1:
                    if len(str(self.danady)) == 1:
                        daty3.append("{}0{}01".format(self.danary, self.danamy))
                        daty3.append("{}0{}0{}".format(self.danary, self.danamy, self.danady))
                    else:
                        daty3.append("{}0{}01".format(self.danary, self.danamy))
                        daty3.append("{}0{}{}".format(self.danary, self.danamy, self.danady))
                else:
                    if len(str(self.danady)) == 1:
                        daty3.append("{}{}01".format(self.danary, self.danamy))
                        daty3.append("{}{}0{}".format(self.danary, self.danamy, self.danady))
                    else:
                        daty3.append("{}{}01".format(self.danary, self.danamy))
                        daty3.append("{}{}{}".format(self.danary, self.danamy, self.danady))
            else:
                if len(str(self.danamy)) == 1:
                    if len(str(self.danady)) == 1:
                        daty3.append("{}0{}01".format(self.danary, self.danamy))
                    else:
                        daty3.append("{}0{}01".format(self.danary, self.danamy))
                else:
                    if len(str(self.danady)) == 1:
                        daty3.append("{}{}01".format(self.danary, self.danamy))
                    else:
                        daty3.append("{}{}01".format(self.danary, self.danamy))
        return(daty3)
