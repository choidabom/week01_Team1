# 2309: 일곱 난쟁이
# 일곱난쟁이의 키의 합 = 100
# 아홉 난쟁이의 키는 모두 다름
# 1. 조합의 합이 100되는 경우의 수
# 2. 두 명 값을 빼면 100

import sys
import itertools

num_list = [int(sys.stdin.readline()) for _ in range(9)]
num_list.sort()

nCr = list(itertools.combinations(num_list, 7))
# print(nCr)

for i in range(len(nCr)):
    if sum(nCr[i]) == 100:
        # print(nCr[i])
        # print(sum(nCr[i]))
        for j in nCr[i]:
            print(j)
        break
