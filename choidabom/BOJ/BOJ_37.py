# 10819: 차이를 최대로
# N개의 정수로 이루어진 배열 A
# 첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력
import sys
from itertools import permutations
sys.stdin = open('choidabom\BOJ\input.txt', 'r')
N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))

per_list = permutations(A_list)

answer =0

for i in per_list:
    sum_list = 0
    for j in range(len(i)-1):
        sum_list += abs(i[j]-i[j+1])
    if sum_list > answer:
        answer = sum_list
print(answer)


# for i in range(len(A_list)-1):
#     for j in range():

#     num_list.append(int(A_list[i]))
#     num_list.sort()
# print(num_list)
