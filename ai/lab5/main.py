from Solver import Solver

FILENAMES = {
    'easy': 'easy_01_tsp.txt',
    'medium': 'medium_01_tsp.txt',
    'hard': 'hard_01_tsp.txt'
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


def main():
    file = FILENAMES['hard']

    matrix, n = readFile(file)
    problemParams = {
        'matrix': matrix,
        'numberOfNodes': n,
        'iterations': 1000,
        'evaporation': 0.5,
        'pheronomeQuantity': 0.1
    }
    solver = Solver(problemParams)
    a, b = solver.solve()

    print(a)
    print(b)


if __name__ == '__main__':
    main()