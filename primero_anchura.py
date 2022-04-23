# Taken from: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# a sample graph
<<<<<<< HEAD
import time
import pandas as pd
archivo = './Tableros2.xlsx'
tablero = pd.read_excel(archivo, sheet_name='Hoja1')
print(tablero)
graph = {'A': ['B', 'C', 'D',],
         'B': ['A', 'E', 'F'],
=======

graph = {'A': ['B', 'C', 'D'],
         'b': ['A', 'E', 'F'],
>>>>>>> 5e493d9208e9d9159a48eae67124f5ba9f52cb9a
         'C': ['A', 'G', 'H'],
         'D': ['A', 'G', 'H'],
         'E': ['B', 'I'],
         'F': ['B', 'I', 'K'],
         'G': ['C', 'D', 'K'],
         'H': ['C', 'D', 'L'],
         'I': ['E','F', 'J', 'L'],
         'J': ['I', 'K', 'L'],
         'K': ['F', 'G', 'J', 'L'],
         'L': ['H', 'I', 'K']}


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        print (path)
        l = list(set(graph[vertex]) - set(path))
        for next in sorted(l):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

start = time.time_ns()
print ("solution: ", next(bfs_paths(graph, 'A', 'L'))) 
end = time.time_ns()
print("Tiempo en s:", end-start)