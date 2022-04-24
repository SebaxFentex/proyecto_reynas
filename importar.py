import pandas as pd
import numpy as np
archivo = 'Tableros2.xlsx'


def abrir(n):
  #Mij
  #M01
  hoja = "N=" + str(n)
  tablero = pd.read_excel(archivo, sheet_name=hoja, header=None)
  tablero = tablero.to_numpy()
  pos=list()
  for i, v in np.ndenumerate(tablero):
    ls= list(i)
    if(v=='x'):        
        pos.append(ls[0])
  return pos


if (__name__ == "__main__"):
  x=abrir(4)
