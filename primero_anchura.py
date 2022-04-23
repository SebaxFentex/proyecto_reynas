# Taken from: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# a sample graph

import pandas as pd
import importar
import time
import numpy as np

i=0
tablero = importar.abrir(4)
# for i, v in np.ndenumerate(tablero):
#     if(pd.isna(v)):
#         print("xd")

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
#print ("solution: ", next(bfs_paths(graph, 'A', 'L')))
end = time.time_ns()
print("Tiempo en s:", end-start)