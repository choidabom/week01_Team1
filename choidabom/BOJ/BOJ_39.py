# 10971: 외판원 순회 2
# 각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태
# W[i][j]는 도시 i에서 도시 j로 가기 위한 비용

import sys
from itertools import permutations

sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline()) # 도시의 수 N

course_list = []
for i in range(N):
    if i == 0:
        course_list.append(i)
print(course_list)

A = list(sys.stdin.readline().split() for i in range(N))
print(A)
