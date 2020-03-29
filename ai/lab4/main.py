from GA import GA

FILENAMES = {
    'easy': 'easy_03_tsp.txt',
    'medium': 'medium_01_tsp.txt',
    'hard': 'hard_01_tsp.txt'
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
    filename = FILENAMES['easy']
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

    for i in range(gaParam['noGen'] - 1):
        ga.oneGenerationElitism()
    bestChromosome = ga.bestChromosome()
    print(bestChromosome)

if __name__ == '__main__':
    main()
