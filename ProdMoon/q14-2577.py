import sys

inputs = [sys.stdin.readline().strip() for i in range(3)]

mul = int(inputs[0]) * int(inputs[1]) * int(inputs[2])
inputArray = list(str(mul))
outputArray = [0 for i in range(10)]

for i in range(len(inputArray)):
    outputArray[int(inputArray[i])] = outputArray[int(inputArray[i])] + 1

for output in outputArray:
    print(output)