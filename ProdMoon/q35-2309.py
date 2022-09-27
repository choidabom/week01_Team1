from itertools import permutations
import sys, copy

dwarfs = [int(sys.stdin.readline().strip()) for _ in range(9)]

permus = permutations(dwarfs, 7)
answer = [0 for _ in range(7)]

for i in permus:
    if sum(i) == 100:
        answer = copy.deepcopy(i)

sortedA = sorted(answer)
a = ''
for data in sortedA:
    a += str(data) + '\n'
print(a)