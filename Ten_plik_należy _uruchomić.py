import pandas as pd
from Wybor_zagadnienia import Wybor_zagadnienia

Nazwy, Lista = Wybor_zagadnienia.Wybor_zagadnienia()

L = []
for i in Nazwy:
    L.append(pd.read_csv(i, encoding='ISO-8859-1', sep=';', header=0, index_col=None))


dataFrame = pd.concat(L, ignore_index=True)
nazwa_pliku = '{}-{}.csv'.format(Lista[0][0], Lista[-1][-1]) 
dataFrame.to_csv(nazwa_pliku, sep=';', index=False)