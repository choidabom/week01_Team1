import sys

inputs = [sys.stdin.readline().strip() for i in range(9)]

biggest = 0

for i in range(len(inputs)):
    if biggest < int(inputs[i]):
        biggest = int(inputs[i])
        order = i+1

print(biggest)
print(order)