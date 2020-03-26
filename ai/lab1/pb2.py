import math

'''
    Returneaza distanta euclideana dintre doua puncte
    Input: x1, y1, x2, y2 - integer
    Output: dist - double
'''
def getEuclideanDistance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def runPb2():
    print('Give first pair')
    x1 = int(input('x1='))
    y1 = int(input('y1='))
    print('Give second pair')
    x2 = int(input('x2='))
    y2 = int(input('y2='))

    print('Euclidean distance: ' + str(getEuclideanDistance(x1, y1, x2, y2)))

def runPb2Tests():
    print('Start pb 2 tests')
    assert getEuclideanDistance(1, 10, 1, 6) == 4
    assert getEuclideanDistance(5, 2, 7, 2) == 2
    assert getEuclideanDistance(4, 10, 9, 5) == 7.0710678118654755
    print('Finish pb 2 tests')