import sys

testCase = int(sys.stdin.readline().strip())

inputs = [0 for i in range(testCase)]

for i in range(testCase):
    inputs[i] = sys.stdin.readline().split()

for i in range(testCase):
    strings = list(inputs[i][1])
    for j in range(len(strings)):
        for k in range(int(inputs[i][0])):
            print(strings[j],end="")
    print()