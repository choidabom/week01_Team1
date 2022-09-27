import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())
numbers = [0] * n
numbers = list(map(int, sys.stdin.readline().split()))
operators = [0] * 4
operators = list(map(int, sys.stdin.readline().split()))

# 연산자 중복을 확인하기 위해 연산자를 퍼트려줌
oprList = [0] * (n-1)
k = 0
for i in range(4):
    for j in range(operators[i]):
        oprList[k] = i
        k += 1

# 연산자의 가능한 순열(중복값 제거)
permus = list(permutations(oprList, n-1))
cases = list(set(permus))

# 계산해보고 최솟값 최댓값 찾기
minimum = 1000001000
maximum = -1000001000
for case in cases:
    calc = numbers[0]
    for i in range(n-1):
        if case[i] == 0:
            calc = calc + numbers[i+1]
        elif case[i] == 1:
            calc = calc - numbers[i+1]
        elif case[i] == 2:
            calc = calc * numbers[i+1]
        elif case[i] == 3:
            if calc < 0:
                calc = -( abs(calc) // numbers[i+1] )
            else:
                calc = calc // numbers[i+1]
    
    if calc < minimum:
        minimum = calc
    if calc > maximum:
        maximum = calc

print(f'{maximum}\n{minimum}')