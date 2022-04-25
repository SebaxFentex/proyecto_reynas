# Taken from: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# a sample graph

import importar
import time

#############################################################################
n = 4 ########### SELECCIONAR AQUI EL TAMAÑO DEL TABLERO  ###################
#############################################################################

def nextisgoal(next):
    combinacion = importar.strtolista(next)
    for i in range(n):
        j = i+1
        while(j<n):
            fi = combinacion[i][0]
            ci = combinacion[i][1]
            fj = combinacion[j][0]
            cj = combinacion[j][1]

            if(fi == fj or ci == cj or (abs(fi-fj) == abs(ci-cj))):
                return False

            j+=1
    return True

inicio, graph = importar.abrir(n)

def bfs_paths(graph, start):
    #print("grafo recibido:", graph)
    #print("inicio recibido:", start)
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        print (path)
        l = list(set(graph[vertex]) - set(path))
        #print("act:", vertex, "path:", path, "puedeir:", graph[vertex], "yafue:", set(path), "vair:", l, "sorted:", sorted(l), "\n")
        for next in sorted(l):
            if nextisgoal(next):
                yield path + [next]
            else:
                queue.append((next, path + [next]))

start = time.time()
print ("Solucion: ", next(bfs_paths(graph, inicio)))
end = time.time()

print("Tiempo en s:", end-start)