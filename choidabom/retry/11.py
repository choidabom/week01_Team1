import sys

num_list = [sys.stdin.readline().strip() for i in range(9)]

max = 0
for i in range(9):
    if max < int(num_list[i]):
        max = int(num_list[i])
        order = i+1
        
print(max)
print(order)
