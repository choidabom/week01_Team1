import sys

N, X = map(int, sys.stdin.readline().split())
A = sys.stdin.readline().split()
for i in range(len(A)):
    if X > int(A[i]):
        print(A[i], end=" ")