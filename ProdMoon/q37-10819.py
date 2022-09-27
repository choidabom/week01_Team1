import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())

array = list(map(int, sys.stdin.readline().split()))

permus = permutations(array, n)

sumValue = 0

for case in permus:
    temp = 0

    for i in range(len(case)-1):
        temp += abs(case[i]-case[i+1])
    
    if temp > sumValue:
        sumValue = temp

print(sumValue)