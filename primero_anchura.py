from queue import Queue
import pandas as pd
import numpy as np
import os
import time
archivo = 'Tableros2.xlsx'

def abrir(n):
    hoja = "N=" + str(n)
    tablero = pd.read_excel(archivo, sheet_name = hoja, header = None)
    tablero = tablero.to_numpy()
    pos = list()
    
    mesa = [[0]*n for i in range(n)]

    for i, v in np.ndenumerate(tablero):
        ls = list(i)
        if(v == 'x' or v == 'X'):
            mesa[ls[0]][ls[1]] = v
            pos.append((ls[0], ls[1]))
    print("CASO INICIAL:", pos)
    return pos, mesa

def movimientos(reina, mesa, n):
    sentidoFila =    [-1, -1, -1, 0, 1, 1, 1, 0]
    sentidoColumna = [-1, 0, 1, 1, 1, 0, -1, -1]
    cantMov = [i for i in range(1, n)]
    movs = [tuple(reina)]
    # movs.append(reina)
    #f, c = reina
    for f, c in zip(sentidoFila, sentidoColumna): # Para cada posible mov
        for dist in cantMov: #Para cada posible dist
            celdaObjetivo = (reina[0] + (f * dist), reina[1] + (c * dist))
            # print("celdaobj:", celdaObjetivo[0], celdaObjetivo[1])
            if((0 <= celdaObjetivo[0] < n) and (0 <= celdaObjetivo[1] < n)): # Si la celda esta dentro de la mesa
                if(mesa[celdaObjetivo[0]][celdaObjetivo[1]] != 'x' and mesa[celdaObjetivo[0]][celdaObjetivo[1]] != 'X'): # Si la casilla esta vacia
                    movs.append(celdaObjetivo)
                else:
                    break
            else:
                break
    return movs

def conflict(queens):
    for i in range(1, len(queens)):
        for j in range(0, i):
            a, b = queens[i]
            c, d = queens[j]
            if a == c or b == d or abs(a - c) == abs(b - d):
                return True
    return False

def imprimir(queens, n):
    for i in range(n):
        print(' ---' * n)
        for j in range(n):
            p = 'Q' if (i, j) in queens else ' '
            print('| %s ' % p, end='')
        print('|')
    print(' ---' * n)

def reinas(pos, mesa, n):
    cantMovs = 0
    start = time.time()
    queue = Queue()
    movsPrimeraReina = movimientos(([pos[0][0], pos[0][1]]), mesa, n)
    for i in movsPrimeraReina:
        cantMovs += 1
        aux = [i]
        queue.put(aux)

    # print("queue:")
    # for q_item in queue.queue:
    #     print (q_item)
    while not queue.empty():
        solution = queue.get()
        # print("solution:", solution)

        if conflict(solution):
            continue
        if(len(solution) == n):
            print("RESULTADO:", solution)
            end = time.time()
            print("Tiempo:", end-start)
            print("Nodos expandidos:", cantMovs, "\n")
            return solution
        
        mesa = [[0]*n for i in range(n)]

        for i in range(len(solution)):
            mesa[solution[i][0]][solution[i][1]] = 'x'
        
        for i in range(len(solution), n):
            mesa[pos[i][0]][pos[i][1]] = 'x'
        # print("mesa:", mesa)
        

        reinaAExpandir = [pos[len(solution)][0], pos[len(solution)][1]]
        # print("aexp:", reinaAExpandir)
        moves = movimientos(reinaAExpandir, mesa, n)
        # print("moves generated:", moves)
        for i in moves:
            cantMovs += 1
            agg = solution.copy()
            agg.append(i)
            queue.put(agg)

def main():
    n = int(input('Ingrese el tamaño del tablero: '))
    for i in range(10):
        pos, mesa = abrir(n)
        reinas(pos, mesa, n)

if __name__ == '__main__':
    main()
