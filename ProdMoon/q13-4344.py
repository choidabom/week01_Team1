import sys

testCase = int(sys.stdin.readline())

inputs = [sys.stdin.readline().split() for i in range(testCase)]

for i in range(testCase):
    students = int(inputs[i][0])
    sum = 0

    for j in range(1, students+1):
        sum = sum + int(inputs[i][j])
    
    average = sum / students
    greatStudents = 0

    for j in range(1, students+1):
        if int(inputs[i][j]) > average:
            greatStudents = greatStudents + 1

    greatRate = (greatStudents / students)*100
    greatRate = round(greatRate, 3)
    print("{:.3f}%".format(greatRate))
