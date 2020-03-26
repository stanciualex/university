MAX_INT = 10000000


def readFile(matrix, file):
    file = open(file, 'r')
    n = int(file.readline())
    for _ in range(n):
        line = file.readline()
        lineValues = line.split(',')
        lineList = []

        for value in lineValues:
            lineList.append(int(value))

        matrix.append(lineList)

    return n


def minDistance(n, dist, visited):
    min = MAX_INT
    min_index = -1

    for index in range(n):
        if dist[index] < min and index + 1 not in visited and dist[index] != 0:
            min = dist[index]
            min_index = index + 1

    return min, min_index


def solve(matrix, n, src=None, dest=None):
    visited = [src] if src else [1]
    sum = 0

    for i in range(n - 1):
        if len(visited) != n:
            min, min_index = minDistance(n, matrix[visited[-1] - 1], visited)
            sum += min
            visited.append(min_index)

            if (dest and min_index == dest):
                break

    sum += matrix[visited[-1] - 1][visited[0] - 1]

    print(n)
    print(visited)
    print(sum)


def main():
    # file = 'easy_01_tsp.txt'
    # file = 'easy_03_tsp.txt'
    # file = 'medium_01_tsp.txt'
    file = 'hard_01_tsp.txt'

    matrix = []
    n = readFile(matrix, file)

    solve(matrix, n)


if __name__ == '__main__':
    main()
