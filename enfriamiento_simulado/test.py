
from pydoc import doc
from anneal import SimAnneal
import matplotlib.pyplot as plt
import random
from file_controller import read_file

num = 6
while(num != 4 and num != 6 and num != 8):
    num = int(input())

tablero = read_file(num)

def read_coords(path):
    coords = []
    for line in tablero:
        coords.append(line)
    return coords

# def read_coords(path):
#     coords = []
#     with open(path, "r") as f:
#         for line in f.readlines():          
#             line = [float(x.replace("\n", "")) for x in line.split(" ")]
#             coords.append(line)
#     return coords

def generate_random_coords(num_nodes):
    return [[int(random.uniform(0, 4)), int(random.uniform(0, 4))] for i in range(num_nodes)]

if __name__ == "__main__":
    coords = read_coords("D:/OneDrive - Universidad del Magdalena/Documents/Universidad del Magdalena/2022-1/Inteligencia Artificial/proyecto_reynas/enfriamiento_simulado/coord.txt")  # generate_random_coords(100)
    sa = SimAnneal(coords, stopping_iter=5000)
    sa.anneal()
    #sa.visualize_routes()
    #sa.plot_learning()
