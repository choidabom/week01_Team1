caseNum = input()

array = [0 for n in range(int(caseNum))]

for i in range(int(caseNum)):
    array[i] = list(input().split())

for i in range(int(caseNum)):
    result = int(array[i][0])+int(array[i][1])
    print(result)