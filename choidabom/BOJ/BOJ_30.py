# 1074: Z
# N>1 인 경우, 2**N * 2**N인 2차원 배열을 Z모양으로 탐색하려고함.

import sys
sys.stdin = open('choidabom/BOJ/input.txt', 'r')
sys.setrecursionlimit(10**7)
N, r, c = map(int, sys.stdin.readline().split())

cnt = 0
def find_num(N, r, c):
    global cnt
    if(N == 1):
        return 1
    if(r < N//2 and c < N//2):
    #좌표가 1사분면일  
        find_num(N//2, r, c)
    elif(r < N//2 and c >= N//2):
    #좌표가 2사분면일 때
        cnt += N * N // 4
        find_num(N//2, r, c - N//2)
    elif(r >= N//2 and c < N//2):
    #좌표가 3사분면일 때
        cnt += (N * N // 4) * 2
        find_num(N//2, r-N//2, c)
    else:
    #좌표가 4사분면일 때
        cnt += (N * N // 4) * 3
        find_num(N//2, r - N//2, c - N//2)

size = 2 ** N
find_num(size, r, c)
print(int(cnt))