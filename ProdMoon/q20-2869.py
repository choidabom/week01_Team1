import sys, math

inputs = sys.stdin.readline().split()

# a = int(inputs[0])
# b = int(inputs[1])
# v = int(inputs[2])

a,b,v = map(int, inputs)

if a >= v:
    print(1)
else:
    days = (v-a)/(a-b)
    days = math.ceil(days+1)
    print(days)