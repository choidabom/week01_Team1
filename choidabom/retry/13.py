import sys
C = int(sys.stdin.readline())
N = [sys.stdin.readline().split() for i in range(C)]

for i in range(C):
    student_num = int(N[i][0])
    sum = 0
    
    for j in range(1, student_num+1):
        sum += int(N[i][j])

    avg = int(sum / student_num)
    greateStudent = 0

    for j in range(1, student_num+1):
        if int(N[i][j]) > avg:
            greateStudent += 1

    greatRate = (greateStudent/student_num)*100
    greatRate = round(greatRate, 3)
    # 반올림하여 소수점 셋째자리까지 출력
    print("{:.3f}%".format(greatRate))
