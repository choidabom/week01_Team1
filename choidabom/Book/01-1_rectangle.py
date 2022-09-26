# 직사각형 넓이로 변의 길이 구하기
# 약수를 나열하는 프로그램

import sys
N = int(input('직사각형의 넓이를 입력하세요.:'))

for i in range(1, N+1):
    if i * i > N:
        break
    if N % i:
        continue
    print(f'{i} x {N // i}')

