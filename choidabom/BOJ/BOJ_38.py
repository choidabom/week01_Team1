# 10971: 외판원 순회 2
# 각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태

import sys
from itertools import permutations
N = int(sys.stdin.readline()) # 도시의 수 N

# 도시의 수만큼 도시 리스트로 나타내기
course_list = []
for i in range(N):
    course_list.append(i)

# 도시의 수만큼 갈 수 있는 경로 순열로 나타내기
cases = permutations(course_list, N)
# print(cases)

# W[i][j]는 도시 i에서 도시 j로 가기 위한 비용
W = list(sys.stdin.readline().split() for i in range(N))
# print(W)

min_cost = 10000000

for case in cases:
    cost = 0
    check = True
    case = list(case)
    # print(case)
    for i in range(len(case)):
        if int(W[case[i-1]][case[i]]) == 0:
            check = False
            break
        else:
            cost += int(W[case[i-1]][case[i]])
    if check == True:
        if min_cost > cost:
            min_cost = cost
    
print(min_cost)


