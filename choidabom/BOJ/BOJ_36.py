# 2789: 블랙잭

# 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임
# N장의 카드, 숫자 M
# N장의 카드 중에서 3장의 카드 골라야함. 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야함.
# 출력: 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

import sys
import itertools
sys.stdin = open('choidabom\Baekjoon\input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
num_list = map(int, sys.stdin.readline().split())

combi = list(itertools.combinations(num_list, 3))

max = 0
max_list=[]
for i in range(len(combi)):
    if sum(combi[i]) <= M:
        if max <= sum(combi[i]):
            max = sum(combi[i])
            max_list.append(max)
    
print(max_list[-1])