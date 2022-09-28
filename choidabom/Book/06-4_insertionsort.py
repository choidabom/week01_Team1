# 단순 삽입 정렬 알고리즘 구현하기

import sys

num = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for i in range(num)]

def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

insertion_sort(x)

for i in range(num):
    print(x[i])
    