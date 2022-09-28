# 10872: 팩토리얼

import sys

n = int(sys.stdin.readline())

# N! = N * (N-1) * (N-2) * (N-3) * ... * 1

def factorial(n):
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(n))

# for i in range(n, 1, -1):
#     factorial = i * (i-1)
        
