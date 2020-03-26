import networkx

from GA import GA

FILENAMES = {
    'dolphins': 'dolphins.gml',
    # 'football': 'football.gml',
    'karate': 'karate.gml',
    'krebs': 'krebs.gml'
}

def readNetworkFromFile(filename):
    network = {}
    degrees = []
    path = './resources/' + filename
    data = networkx.read_gml(path, label='id')

    network['noNodes'] = data.number_of_nodes()
    network['noEdges'] = data.number_of_edges()
    network['mat'] = networkx.adjacency_matrix(data).todense()
    for node, val in data.degree():
        degrees.append(val)
    network['degrees'] = degrees
    network['graph'] = data

    return network

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']

    M = 2 * noEdges
    Q = 0.0
    for i in range(noNodes):
        for j in range(noNodes):
            if (communities[i] == communities[j]):
                Q += (mat.item(i, j) - degrees[i] * degrees[j] / M)
    return Q * 1 / M

def initParams(filename):
    network = readNetworkFromFile(filename)
    gaParam = {
        'popSize': 300,
        'noGen': 10,
        'network': network
    }
    problParam = {
        'function': modularity,
        'network': network
    }

    return gaParam, problParam

def getNumberOfCommunities(param, repres):
    communities = []

    for _ in range(param['network']['noNodes'] + 1):
        communities.append([])

    for i in range(param['network']['noNodes']):
        communities[repres[i]].append(i + 1)

    i = 0
    counter = 0
    while i < len(communities):
        if len(communities[i]) > 0:
            counter += 1
        i += 1

    return counter

def main():
    gaParam, problParam = initParams(FILENAMES['dolphins'])
    ga = GA(gaParam, problParam)

    ga.initialisation()
    ga.evaluation()

    currentGeneration = 0
    while currentGeneration <= gaParam['noGen']:
        ga.oneGeneration()
        bestChromosome = ga.bestChromosome()

        print('=== [Gen ' + str(currentGeneration) + '] ===')
        print(bestChromosome)
        print('Fitness: ' + str(bestChromosome.fitness))
        print('Number of communities: ' + str(getNumberOfCommunities(problParam, bestChromosome.repres)))
        print('')
        currentGeneration += 1

if __name__ == '__main__':
    main()