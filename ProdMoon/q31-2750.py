import sys

n = int(sys.stdin.readline().strip())
numbers = []

for i in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

numbers.sort()

for i in range(n):
    print(numbers[i])