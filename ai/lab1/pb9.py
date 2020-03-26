'''
    Calculeaza suma submatricii cu coltul stanga-sus in (x1, y1) si coltul dreapta-jos in (x2, y2)
    Input:  matrix - Array of arrays
            x1, y1, x2, y2 - integer, coordonate din matrice
    Output: sum - integer
'''
def calcSum(matrix, x1, y1, x2, y2):
    sum = 0

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            sum += matrix[i][j]

    return sum

def runPb9():
    matrix = [[0, 2, 5, 4, 1],
              [4, 8, 2, 3, 7],
              [6, 3, 4, 6, 2],
              [7, 3, 1, 8, 3],
              [1, 5, 7, 9, 4]]

    print('Give first coordinate')
    x1 = input('x1=')
    y1 = input('y1=')
    print('Give second coordinate')
    x2 = input('x2=')
    y2 = input('y2=')

    print('Sum: ' + calcSum(matrix, x1, y1, x2, y2))


def runPb9Tests():
    matrix = [[0, 2, 5, 4, 1],
              [4, 8, 2, 3, 7],
              [6, 3, 4, 6, 2],
              [7, 3, 1, 8, 3],
              [1, 5, 7, 9, 4]]

    print('Start pb 9 tests')
    assert calcSum(matrix, 0, 0, 1, 1) == 14
    assert calcSum(matrix, 1, 1, 3, 2) == 21
    assert calcSum(matrix, 2, 3, 4, 4) == 32
    print('Finish pb 9 tests')