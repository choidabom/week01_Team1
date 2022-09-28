# 1978: 소수 찾기

import sys

N = int(sys.stdin.readline()) 
testCase = list(map(int, sys.stdin.readline().split()))
count = 0

for i in range(len(testCase)):
    num = int(testCase[i])
    sosu = True

    if num == 1:
        sosu = False

    for j in range(2, num):
        if num == 2 or num == 3:
            sosu = True
        elif num % j == 0:
            sosu = False

    if sosu == True:
        count += 1
        # print('{}은 소수입니다.'.format(num))
    else:
        count += 0
        # print('{}은 소수가 아닙니다.'.format(num))

print(count)