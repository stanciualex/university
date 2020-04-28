from Solver import Solver
import math

FILENAMES = {
    'easy': 'easy_01_tsp.txt',
    'medium': 'medium_01_tsp.txt',
    'hard': 'hard_01_tsp.txt',
    'berlin': 'berlin52.txt'
}

def readFile(file):
    matrix = []
    file = open('resources/' + file, 'r')
    n = int(file.readline())
    for _ in range(n):
        line = file.readline()
        lineValues = line.split(',')
        lineList = []

        for value in lineValues:
            lineList.append(int(value))

        matrix.append(lineList)

    return matrix, n

def readBerlin(filename):
    with open('resources/' + filename) as file:
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

    return mat, len(mat)


def main():
    file = FILENAMES['berlin']

    matrix = {}
    n = None
    if file == FILENAMES['berlin']:
        matrix, n = readBerlin(file)
    else:
        matrix, n = readFile(file)
    problemParams = {
        'matrix': matrix,
        'numberOfNodes': n,
        'iterations': 100,
        'evaporation': 0.5,
        'pheronomeQuantity': 0.1
    }
    solver = Solver(problemParams)
    a, b = solver.solve()

    print(a)
    print(b)


if __name__ == '__main__':
    main()