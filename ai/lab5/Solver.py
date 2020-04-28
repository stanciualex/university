import random
from Ant import Ant
import matplotlib.pyplot as plt

class Solver:
    def __init__(self, problemParams):
        self.__matrix = problemParams['matrix']
        self.__numberOfNodes = problemParams['numberOfNodes']
        self.__trails = [[0 for _ in range(self.__numberOfNodes)] for _ in range(self.__numberOfNodes)]
        self.__iterations = problemParams['iterations']
        self.__evaporation = problemParams['evaporation']
        self.__pheronomeQuantity = problemParams['pheronomeQuantity']

    def init(self):
        cities = [i for i in range(1, self.__numberOfNodes + 1)]
        random.shuffle(cities)
        self.__ants = [Ant(i) for i in cities]

    def getNeighborNodesProbabilities(self, ant):
        probabilities = []
        currentCity = ant.getCities()[-1]
        pheromone = 0

        for i in range(0, self.__numberOfNodes):
            if not ant.isVisited(i + 1):
                pheromone += self.__trails[currentCity - 1][i] + 1.0 / self.__matrix[currentCity - 1][i]

        for i in range(0, self.__numberOfNodes):
            if ant.isVisited(i + 1):
                probabilities.append(0)
            else:
                n = self.__trails[currentCity - 1][i] + 1.0 / self.__matrix[currentCity - 1][i]
                probabilities.append(n / pheromone)

        return probabilities

    def getMostLikelyNodeToVisit(self, probabilities):
        randomValue = random.uniform(0, 1)
        totalValue = 0
        for i in range(0, self.__numberOfNodes):
            totalValue += probabilities[i]
            if randomValue <= totalValue:
                return i + 1

    def moveAnts(self):
        for ant in self.__ants:
            neighborNodeProbabilities = self.getNeighborNodesProbabilities(ant)
            ant.appendCity(self.getMostLikelyNodeToVisit(neighborNodeProbabilities))

    def updateTrails(self):
        for i in range(0, self.__numberOfNodes):
            for j in range(0, self.__numberOfNodes):
                self.__trails[i][j] *= self.__evaporation

        for ant in self.__ants:
            antCities = ant.getCities()
            self.__trails[antCities[-2] - 1][antCities[-1] - 1] += self.__pheronomeQuantity

    def updateBestTrail(self, bestTrail, bestTrailLength):
        for ant in self.__ants:
            trailLength = ant.getTrailWeight(self.__matrix)
            if (trailLength < bestTrailLength):
                bestTrailLength = trailLength
                bestTrail = ant.getCities()

        return bestTrail, bestTrailLength

    def solve(self):
        bestTrail = []
        bestTrailLength = 9999999

        bestTrailsArr = []
        for _ in range(0, self.__iterations):
            self.init()
            while len(self.__ants[0].getCities()) < self.__numberOfNodes:
                self.moveAnts()
                self.updateTrails()
            bestTrail, bestTrailLength = self.updateBestTrail(bestTrail, bestTrailLength)
            bestTrailsArr.append(bestTrailLength)

        plt.plot(bestTrailsArr)
        plt.ylabel('Best trail length')
        plt.xlabel('Iteration')
        plt.show()

        return bestTrail, bestTrailLength

