# 14888: 연산자 끼워넣기

# 준호오빠 코드
import sys
from itertools import permutations
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
N = int(sys.stdin.readline().strip())
num_list = [0] * N
num_list = list(map(int, sys.stdin.readline().split()))
operator = [0] * (N-1)
operator = list(map(int, sys.stdin.readline().split()))

# 인덱스 갯수에 따라 연산자 넣어주기
oper_list = [0] * (N-1)
num = 0
for i in range(4):
    # operator[i] 요소의 개수만큼 반복문이 돌아서 리스트에 넣어줌
    for j in range(operator[i]):
        oper_list[num] = i
        num += 1

# 연산자의 가능한 순열(중복값 제거)
cases = list(set(permutations(oper_list, N-1)))
print(cases)

minimum = 1000001000
maximum = -1000001000
for case in cases:
    calc = num_list[0]
    for i in range(N-1):
        if case[i] == 0:
            calc = calc + num_list[i+1]
        if case[i] == 1:
            calc = calc - num_list[i+1]
        elif case[i] == 2:
            calc = calc * num_list[i+1] 
        elif case[i] == 3:
            if calc < 0:
                calc = -(abs(calc)//num_list[i+1])
            else:
                calc = calc // num_list[i+1]

    if calc < minimum:
        minimum = calc
    if calc > maximum:
        maximum = calc

print(maximum, minimum)   

# oper_list = []
# for idx in operator:
#     if idx == 0:
#         for j in range(len(N-1)):
#             oper_list.append(operator[j])
#     elif idx == 1:
#         for j in range(len(N-1)):
#             oper_list.append(operator[j])
#     elif idx == 2:
#         for j in range(len(N-1)):
#             oper_list.append(operator[j])
#     else:
#         for j in range(len(N-1)):
#             oper_list.append(operator[j])



# print(N)
# print(num_list)
# print(operator)
# print(oper_list)