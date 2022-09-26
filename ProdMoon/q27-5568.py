import sys, copy

allCardsNum = int(sys.stdin.readline().strip())
chooseCardsNum = int(sys.stdin.readline().strip())

global answers
global making

cards = []
answers = ['0']
making = []

for i in range(allCardsNum):
    cards.append(sys.stdin.readline().strip())


def depth(cardArray, n):
    global answers
    global making

    if n == 0:
        temp = list(map(str, making))
        temp = ''.join(temp)
        for i in range(0, len(answers)):
            if answers[i] == temp:
                temp = False
                break
        if temp != False:
            answers.append(temp)
    else:
        for i in range(len(cardArray)):
            making.append(cardArray[i])
            temp = copy.deepcopy(cardArray)
            del temp[i]
            depth(temp, n-1)
            del making[len(making)-1]
    

depth(cards, chooseCardsNum)
print(len(answers)-1)