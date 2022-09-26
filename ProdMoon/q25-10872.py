import sys

n = int(sys.stdin.readline().strip())

if n == 0:
    print(1)
else:
    result = n
    while n != 1:
        result = result * (n - 1)
        n = n - 1

    print(result)