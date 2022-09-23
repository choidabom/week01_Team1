import sys

testCase = int(sys.stdin.readline())

inputs = [list(sys.stdin.readline().strip()) for i in range(testCase)]

for input in inputs:
    score = 0
    win = 0
    for case in input:
        if case == 'O':
            win = win + 1
            score = score + win
        else:
            win = 0
    print(score)