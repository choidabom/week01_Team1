import sys, copy
from itertools import permutations

n = sys.stdin.readline().split()

n, m = int(n[0]), int(n[1])

cards = sys.stdin.readline().split()
cards = list(map(int, cards))

permus = permutations(cards, 3)

nearest = 0

for case in permus:
    if abs(m - nearest) >= abs(m - sum(case)) and sum(case) <= m :
        nearest = sum(case)

print(nearest)