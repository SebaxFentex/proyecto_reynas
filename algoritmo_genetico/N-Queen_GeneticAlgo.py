import random
import importar

mutation_probability = 0.15
def random_chromosome(size): #making random chromosomes 
    # return [ random.randint(1, nq) for _ in range(nq) ]
    return importar.abrir(size)
    #return [2,0,3,1]

def fitness(chromosome):
    #suma todas las colisiones horizontales, cada colision es una arista, por tanto por reina la cuenta doble
    horizontal_collisions = sum([chromosome.count(queen)-1 for queen in chromosome])/2

    diagonal_collisions = 0

    n = len(chromosome)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    # determina la cantidad de colisiones en las diagonales descendentes y ascendentes
    for i in range(n):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[len(chromosome) - i + chromosome[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
    #   retorna el valor maximo del fitness menos la cantidad de colisiones
    a=diagonal_collisions
    c=int(maxFitness - (horizontal_collisions + diagonal_collisions))
    b=10
    return int(maxFitness - (horizontal_collisions + diagonal_collisions)) #28-(2+3)=23

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
    populationWithProbabilty = zip(population, probabilities)
    total = sum(w for c, w in populationWithProbabilty)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(population, probabilities):
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"
        
def reproduce(x, y): #doing cross_over between two chromosomes
    n = len(x)
    c = random.randint(0, n - 1)
    return x[0:c] + y[c:n]

def mutate(x):  #randomly changing the value of a random index of a chromosome
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n-1)
    x[c] = m
    return x

def genetic_queen(population, fitness):
    new_population = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = random_pick(population, probabilities) #best chromosome 1
        y = random_pick(population, probabilities) #best chromosome 2
        child = reproduce(x, y) #creating two new chromosomes from the best 2 chromosomes
        if random.random() < mutation_probability:
            child = mutate(child)
        #print_chromosome(child)
        new_population.append(child)
        if fitness(child) == maxFitness: break
        #print(i)
    return new_population

def print_chromosome(chrom):
    print("Chromosome = {},  Fitness = {}"
        .format(str(chrom), fitness(chrom)))


if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: ")) #say N = 8
    maxFitness = ((nq*(nq-1))/2)  # n*(n-1)/2 = (para n=8, 28; para n=4, 6;para n=12 ,66)
    population = [random_chromosome(nq) for _ in range(100)] 
    
    promedioFitness=0.0
    generation = 1
    higherFitness=0
    MAXGENERATION = 1000
    while not maxFitness in [fitness(chrom) for chrom in population] and generation<=MAXGENERATION:
        print("=== Generation {} ===".format(generation))
        population = genetic_queen(population, fitness)
        print("")
        higherFitness=max([fitness(n) for n in population])
        print("Maximum Fitness = {}".format(higherFitness))
        generation += 1
        promedioFitness=sum(fitness(chrom) for chrom in population)
    chrom_out = []
    if(generation<MAXGENERATION):
        print("Solucionado en la generacion {}!".format(generation-1))
    else:
        print("Se llegó a la máxima iteracion sin obtener una solución")
        maxFitness=higherFitness

    for chrom in population:
        if fitness(chrom) == maxFitness:
            print("")
            print('_________________________')
            print("El mejor candidato de la generación: ")
            chrom_out = chrom
            print_chromosome(chrom)
            print('_________________________')
    for i in population:
        print_chromosome(i)
            
    # board = []

    # for x in range(nq):
    #     board.append(["x"] * nq)
        
    # for i in range(nq):
    #     board[nq-chrom_out[i]][i]="Q"
            

    # def print_board(board):
    #     for row in board:
    #         print (" ".join(row))
            
    # print()
    # print_board(board)
            
           
            
    

