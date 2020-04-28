class Ant:
    def __init__(self, startCity):
        self.__cities = [startCity]

    def appendCity(self, city):
        self.__cities.append(city)

    def getCities(self):
        return self.__cities

    def isVisited(self, city):
        return city in self.__cities

    def getTrailWeight(self, matrix):
        length = 0

        for i in range(0, len(self.__cities) - 1):
            length += matrix[self.__cities[i] - 1][self.__cities[i + 1] - 1]
        length += matrix[self.__cities[-1] - 1][self.__cities[0] - 1]

        return length