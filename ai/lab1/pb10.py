def getNumberOfOnes(arr):
    left = 0
    n = right = len(arr)

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0)):
            return n - mid
        elif (arr[mid] == 1):
            right = mid - 1
        else:
            left = mid + 1

'''
    Returneaza linia din matrice care contine cele mai multe valori de 1
    Input: matrix - Array of arrays
    Ouput: lineIndex - integer
'''
def getMaxLineIndex(matrix):
    lineIndex = -1
    maxOnes = -1

    for index, line in enumerate(matrix):
        sum = getNumberOfOnes(line)
        # sum = 0
        # for num in line:
        #     sum += num
        if sum > maxOnes:
            maxOnes = sum
            lineIndex = index

    return lineIndex

def runPb10():
    matrix = [[0, 0, 0, 1, 1],
              [0, 1, 1, 1, 1],
              [0, 0, 1, 1, 1]]

    lineIndex = getMaxLineIndex(matrix)

    print(matrix[lineIndex])

def runPb10Tests():
    matrix = [[0, 0, 1, 1, 1],
              [0, 0, 0, 1, 1],
              [0, 0, 1, 1, 1],
              [1, 1, 1, 1, 1]]

    print('Start pb 10 tests')
    assert getMaxLineIndex(matrix) == 3
    print('Finish pb 10 tests')