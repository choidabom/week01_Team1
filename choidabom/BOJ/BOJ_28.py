# 1914: 하노이 탑

# 1. 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 2. 쌓아놓은 원판은 항상 위의 것이 아래의 것보다 작아야한다.
# 이 작업을 수행하는데 필요한 이동 순서 출력 프로그램 => 이동 횟수 최소


# 출력: 첫째 줄에 옮긴 횟수 K 출력
# N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행과정 출력
# 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력,
# 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

# 로직은 100%로 이해했지만 재귀로 짜는 방법을 모르겠다.

import sys
# 입력: 첫 번째 장대에 쌓인 원판의 개수 N(1<=N<=100)
n = int(sys.stdin.readline())

# 6 = 1 + 2 + 3
def move(n, x, y):
    if n > 1:
        move(n-1, x, 6-x-y)
    print(x, y)
    if n > 1:
        move(n-1, 6-x-y, y)

# 등비수열
# 3, 7, 15, 31 ...
count = 2**n-1
if n > 20:
    print(count)
else:
    print(count)
    move(n, 1, 3)

# 재귀는 어떻게 쓰는거지??????
# def hanoitop(n):
#     result = 3
#     for i in range(2, n+1):
#         if i == n:
#             print(result)
#             break
#         elif i >= 2:
#             result = 2 * result + 1
#             # hanoitop(n+1)
