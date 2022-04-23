import pandas as pd
archivo = 'Tableros2.xlsx'

def abrir(n):
  
  hoja = "N=" + str(n)
  tablero = pd.read_excel(archivo, sheet_name=hoja, header=None)
  tablero.to_csv('Tablero1.csv', encoding='utf-8')
  tablero = tablero.to_numpy()
  return tablero

if (__name__ == "__main__"):
  abrir()
