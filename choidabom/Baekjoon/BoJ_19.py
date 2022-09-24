# 2908: 상수
# 734 893 => 437 398
# 상수의 대답을 출력

import sys

num = sys.stdin.readline().split()
num[0] = int(num[0][::-1])
num[1] = int(num[1][::-1])

if(num[0]>num[1]):
    print(num[0])
else:
    print(num[1])