inputVal = input().split()

inputNumbers = input().split()

for i in range(int(inputVal[0])):
    if int(inputNumbers[i]) < int(inputVal[1]):
        print(inputNumbers[i],end=' ')