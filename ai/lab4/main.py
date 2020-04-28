from GA import GA
import math
import matplotlib.pyplot as plt

FILENAMES = {
    'easy': 'easy_03_tsp.txt',
    'medium': 'medium_01_tsp.txt',
    'hard': 'hard_01_tsp.txt',
    'berlin': 'berlin52.txt'
}


def readFile(file):
    network = {}

    file = open(file, 'r')
    n = int(file.readline())
    network['noNodes'] = n

    matrix = []
    for _ in range(n):
        line = file.readline()
        lineValues = line.split(',')
        lineList = []

        for value in lineValues:
            lineList.append(int(value))

        matrix.append(lineList)
    network['mat'] = matrix

    return network


def readBerlin(filename):
    file = open(filename, 'r')

    content = [line.strip().split(' ') for line in file.readlines()]
    coords = [[int(float(number)) for number in coord] for coord in content]

    mat = [[0 for _ in range(len(coords))] for _ in range(len(coords))]
    for coord in coords:
        m = coord[0]
        mx = coord[1]
        my = coord[2]

        for neighbor in coords:
            n = neighbor[0]
            nx = neighbor[1]
            ny = neighbor[2]

            mat[m - 1][n - 1] = math.sqrt((mx - nx) ** 2 + (my - ny) ** 2)

    network = {
        'mat': mat,
        'noNodes': len(mat)
    }
    return network


def pathFunction(repres, network):
    sum = 0
    matrix = network['mat']
    n = network['noNodes']

    for i in range(n - 1):
        currentNode = repres[i]
        nextNode = repres[i + 1]
        sum += matrix[currentNode - 1][nextNode - 1]
    sum += matrix[repres[-1] - 1][repres[0] - 1]

    return sum


def main():
    filename = FILENAMES['berlin']

    network = None
    if filename == FILENAMES['berlin']:
        network = readBerlin('./resources/' + filename)
    else:
        network = readFile('./resources/' + filename)
    gaParam = {
        'popSize': 10,
        'noGen': 1000,
        'network': network
    }
    problParam = {
        'function': pathFunction,
        'noNodes': network['noNodes']
    }

    ga = GA(gaParam, problParam)
    ga.initialisation()
    ga.evaluation()

    bestFitness = []
    for i in range(gaParam['noGen'] - 1):
        ga.oneGenerationElitism()
        bestFitness.append(ga.bestChromosome().fitness)

    bestChromosome = ga.bestChromosome()
    print(bestChromosome)

    plt.plot(bestFitness)
    plt.ylabel('Best fitness')
    plt.xlabel('Generation')
    plt.show()

if __name__ == '__main__':
    main()
