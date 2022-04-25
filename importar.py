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
  mesa = [ [0]*n for i in range(n)]

  for i, v in np.ndenumerate(tablero):
    ls= list(i)
    if(v == 'x'):
      mesa[ls[0]][ls[1]] = v
      pos.append([ls[0], ls[1]])
  
  return generargrafo(pos, mesa, n)

# ArribaIzq, Arriba, ArribaDer, Der, Abajoder, Abajo, AbajoIzq, Izq
sentidoFila = [-1, -1, -1, 0, 1, 1, 1, 0]
sentidoColumna = [-1, 0, 1, 1, 1, 0, -1, -1]

def generargrafo(pos, mesa, n):
  caminoObstruido = False
  grafo = {}
  reinas = [i for i in range(0, n)] # Lista de 0 a n
  cantMov = [i for i in range(1, n)] # Lista de 1 a n-1

  for i in reinas: # Ejecuta por cada reina que exista
    posReina = [pos[i][0], pos[i][1]] # [x,y] de la reina i

    for f, c in zip(sentidoFila, sentidoColumna): # Ejecuta por cada posible movimiento de las reinas
      print("\nRfila: ", f, " RCol: ", c)
      for dist in cantMov: # Ejecuta por cada posible distancia a mover (de 1 a n-1)
        obj = [(posReina[0] + (f * dist)), (posReina[1] + (c * dist))] # La casilla objetivo
        print("obj:",obj)
        print("posreina:", posReina, " objetivo: ", obj, " dist:", dist)
        objdentro = ((0 <= obj[0] < n) and (0 <= obj[1] < n))
        print("el obj esta dentro del tablero?", objdentro)
        if(objdentro): # Si el mov esta dentro del tablero
          print("contenido de ", obj, ": ", mesa[obj[0]][obj[1]])
          if(mesa[obj[0]][obj[1]] != 'x'): # Si la casilla objetivo esta vacia
            
            posreinas = ""
            for x in pos:
              posreinas = posreinas + str(x[0]) + str(x[1])
            print("posreinas:", posreinas)
            print("posreinas not in grafo?", (posreinas not in grafo))
            if(posreinas not in grafo):
              grafo[posreinas] = []
            print("grafo:", grafo)

            agregar = posreinas
            agregar = list(agregar)
            agregar[i*2] = str(obj[0])
            agregar[(i*2) + 1] = str(obj[1])
            agregar = ''.join(agregar)

            print("valor q se agrega al grafo: ", agregar)

            grafo[posreinas].append(agregar)

            print("grafo:", grafo, "\n")
            
          else: # Si la casilla objetivo no esta vacia
            caminoObstruido = True
            break
        else:
          break
      # del f, c
        
        


        
  return grafo
  


    


# def validarCasilla()

if (__name__ == "__main__"):
  x=abrir(4)
  print(x)
