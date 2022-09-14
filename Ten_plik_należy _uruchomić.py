import pandas as pd
from Wybor_zagadnienia import Wybor_zagadnienia

file=Wybor_zagadnienia.Wybor_zagadnienia()

L = []
for i in file:
    L.append(pd.read_csv(i, encoding='ISO-8859-1', sep=';', header=0, index_col=None))

dataFrame = pd.concat(L, ignore_index=True)
dataFrame.to_csv('Polaczone.csv', sep=';', index=False)