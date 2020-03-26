'''
    Returneaza cuvintele care apar o singura data in text
    Input: text - string
    Output: sol - array de string-uri
'''
def getWords(text):
    wordsDict = {}
    sol = []

    for word in text.split(' '):
        if word in wordsDict.keys():
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1

    for key, value in wordsDict.items():
        if value == 1:
            sol.append(key)

    return sol

def runPb4():
    text = 'ana are ana are mere rosii ana'

    words = getWords(text)
    for word in words:
        print(word)

def runPb4Tests():
    print('Start pb 4 tests')
    text1 = 'facultate smechera facultate info smechera popandau'
    words1 = getWords(text1)
    assert words1[0] == 'info'
    assert words1[1] == 'popandau'

    text2 = 'ana are mere ana are mere'
    words2 = getWords(text2)
    assert len(words2) == 0
    print('Finish pb 4 tests')