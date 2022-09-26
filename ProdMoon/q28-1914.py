import sys

def hanoi(n, here, there, neutral):
    if n == 1:
        print(here, there)
    else:
        hanoi(n-1, here, neutral, there)
        print(here, there)
        hanoi(n-1, neutral, there, here)

        
n = int(sys.stdin.readline().strip())

count = 2**n - 1

if n > 20:
    print(count)
else:
    print(count)
    hanoi(n, 1, 3, 2)