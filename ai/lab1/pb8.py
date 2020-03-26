'''
    Converteste un numar din reprezentarea decimala in cea binara
    Input: n - integer
    Output: binaryString - string
'''
def decimalToBinary(n):
    binaryString = ''
    while n:
        binaryString = str(n % 2) + binaryString
        n //= 2
    return binaryString

def runPb8():
    n = input('Give n:')

    for i in range(n):
        print(decimalToBinary(i + 1))

def runPb8Tests():
    print('Start pb 8 tests')
    assert decimalToBinary(100) == '1100100'
    assert decimalToBinary(58) == '111010'
    assert decimalToBinary(27) == '11011'
    print('Finish pb 8 tests')