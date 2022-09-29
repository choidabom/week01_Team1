import sys
x, y, w, h = map(int, sys.stdin.readline().split())

value_list = []
value_list.append(x)
value_list.append(w-x)
value_list.append(y)
value_list.append(h-y)

value_list.sort()
print(value_list[0])