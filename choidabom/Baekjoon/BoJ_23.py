# 1065: 한수
# 양의 정수 X의 각 자리가 등차수열을 이룸 => 한수
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수

# 1. 숫자를 잘라야함.
# 2. 일단 등차수열을 구하는 방법을 먼저 생각하기
# 한 자리수도, 두 자리수도 등차
# 0, 음수, 양수
# [1, 2, 3, 4]

import sys
N = int(sys.stdin.readline())

cha = 0
tmp = [] # 등차 모음
count = 0 # 한수

for num in range(1, N+1):
    tmp = [] # 등차 모음
    # print('값: ', num)
    num_list = list(map(int, str(num)))
    # print('값 나누기: ', num_list)
    for i in range(len(num_list)):
        if len(num_list) == 1 or len(num_list) == 2: # 한 자리수 
            tmp.append(num_list)
            break
        else:
            if i == len(num_list) - 1:
                break
            else:
                cha = num_list[i] - num_list[i+1]
                tmp.append(cha)
                # print(cha)
    # print(tmp)

    for i in range(len(tmp)):
        if len(tmp) == 1: # 한 자리수 
            count += 1
            break
        elif len(tmp) >= 2: # 두 자리수
            if tmp[i] == tmp [i+1]:
                count += 1
                break
            else:
                count += 0
                break
    
print(count)

# 입력 110
# 출력 99


# 등차수열
# num_list = list(map(int, str(N)))
# for i in range(len(num_list)):
#     if len(num_list) == 1 or len(num_list) == 2: # 한 자리수 
#         tmp.append(num_list)
#         break
#     else:
#         if i == len(num_list)-1:
#             break
#         else:
#             cha = num_list[i] - num_list[i+1]
#             tmp.append(cha)
#             # print(cha)

# for i in range(len(tmp)):
#     if len(tmp) == 1: # 한 자리수 
#         count += 1
#         print('등차수열 입니다.')
#         break
#     elif len(tmp) >= 2: # 두 자리수
#         if tmp[i] == tmp [i+1]:
#             print('등차수열 입니다.')
#             count += 1
#             break
#         else:
#             print('등차수열이 아닙니다.')
#             break
# print(count)
