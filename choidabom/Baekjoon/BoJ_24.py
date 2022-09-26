# 2628: 종이자르기

import sys

x, y = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
inputs = [sys.stdin.readline().split() for i in range(n)]

width_tmp = [0]
height_tmp = [0]
width_tmp.append(x)
height_tmp.append(y)

for i in range(len(inputs)):
    if int(inputs[i][0]) == 0:
        height_tmp.append(int(inputs[i][1]))
    elif int(inputs[i][0]) == 1:
        width_tmp.append(int(inputs[i][1]))
      
width_tmp.sort()
height_tmp.sort()

# print('가로 자르기: ', width_tmp)
# print('세로 자르기: ', height_tmp)

max_width = 0
max_height = 0

for i in range(1, len(width_tmp)):
    tmp = width_tmp[i] - width_tmp[i-1]

    if len(width_tmp) == 1:  # 세로로 한 번도 자르지 않을 경우
        max_width = width_tmp[-1]
        break
    else: # 세로로 한 번이라도 자른 경우
        if tmp >= max_width:
            max_width = tmp
            
        else:
            pass

for i in range(1, len(height_tmp)):
    tmp2 = height_tmp[i] - height_tmp[i-1]
    if len(height_tmp) == 1:  # 가로로 한 번도 자르지 않을 경우
        max_height = height_tmp[-1]
        break
    else: # 가로로 한 번이라도 자른 경우
        if tmp2 >= max_height:
            max_height = tmp2
        else:
            pass

print(max_width*max_height)

# 입력
# 10 8
# 3
# 0 3
# 1 4
# 0 2

# 출력
# 30

# 입력 2
# 7 10
# 4
# 0 2
# 1 3
# 0 4
# 0 8

# 출력 2
# 16