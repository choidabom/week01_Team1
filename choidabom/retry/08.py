import sys
# n: 테스트 케이스의 개수
n = int(sys.stdin.readline())
A = [sys.stdin.readline().split() for _ in range(n)]

for i in range(n):
    print(int(A[i][0]) + int(A[i][1]))