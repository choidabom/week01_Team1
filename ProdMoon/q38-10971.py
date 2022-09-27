import sys
from itertools import permutations

n = int(sys.stdin.readline().strip())

w = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    w[i] = list(map(int, sys.stdin.readline().split()))

cityList = [i for i in range(n)]
ways = permutations(cityList, n)
leastCost = 1000000 * 11

for way in ways:
    cost = 0
    check = True
    j = 1
    for i in range(n):
        if w[way[i]][way[j]] == 0:
            check = False
            break
        else:
            cost += w[way[i]][way[j]]
            if j == n-1 : j = 0
            else : j += 1
    
    if check == True:
        if leastCost > cost:
            leastCost = cost

print(leastCost)
