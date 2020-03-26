from pb2 import runPb2, runPb2Tests
from pb4 import runPb4, runPb4Tests
from pb8 import runPb8, runPb8Tests
from pb9 import runPb9, runPb9Tests
from pb10 import runPb10, runPb10Tests

def runTests():
    runPb2Tests()
    runPb4Tests()
    runPb8Tests()
    runPb9Tests()
    runPb10Tests()

def main():
    # runPb2()
    # runPb4()
    # runPb8()
    # runPb9()
    # runPb10()
    runTests()

if __name__ == '__main__':
    main()