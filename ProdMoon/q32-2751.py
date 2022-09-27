import sys

n = int(sys.stdin.readline().strip())

numbers = [0] * n

for i in range(n):
    numbers[i] = int(sys.stdin.readline().strip())

numbers.sort()

result = ""

for i in range(n):
    result += (str(numbers[i]) + '\n')

print(result)