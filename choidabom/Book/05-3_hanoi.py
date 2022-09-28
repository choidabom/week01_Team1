# # 하노이 탑 구현하기

# def move(no:int, x:int, y:int) -> None:
#     if no > 1:
#         move(no-1, x, 6-x-y)
    
#     print(f'원반 [{no}을(를) {x} 기둥에서 {y} 기둥으로 옮깁니다.')
#     if no > 1:
#         move(no-1, 6-x-y, y)

# print('하노이 탑을 구현합니다.')
# n = int(input('원반의 개수를 입력하세요.: '))
# move(n, 1, 3)

import sys
N = int(sys.stdin.readline())

def f(n, a, b, c):
    if (n == 1):
        print(a, c, sep = " ")
    else:
        f(n-1, a, c, b)
        f(1, a, b, c)
        f(n-1, b, a, c)

print(2**N-1)

if (N <=20):
    f(N, 1, 2, 3)