# 4344: 평균은 넘겠지
import sys

# 첫째 줄 => 테스트 케이스의 개수 C
# 둘째 줄 => 각 테스트 케이스마다 학생의 수 N, N명의 점수

# 하나의 값만 입력받을 때
testCase =  int(sys.stdin.readline())

# testCase 개수에 따라 입력이 여러 줄로 들어옴
inputs = [sys.stdin.readline().split() for i in range(testCase)]

# 여러 줄이니깐 for문이겠지? 먼저 크게 한 바퀴 돌거 같으니깐 testCase...!?
for i in range(testCase):
    # inputs의 첫 번째 값이 학생의 수 N
    N = int(inputs[i][0])
    sum = 0
    # range(시작 숫자, 끝 숫자)
    # inputs = ['5', '50', '50', '70', '80', '100']
    
    # 학생의 평균을 구하기 위한 학생 점수 총합
    for j in range(1, N+1):
        sum = sum + int(inputs[i][j])
    
    avg = sum / N # 학생들 점수 평균

    # 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
    greatStudents = 0
        
    for j in range(1, N+1):
        if int(inputs[i][j]) > avg:
            greatStudents += 1

    greatRate = (greatStudents / N)*100
    greatRate = round(greatRate, 3)
    print("{:.3f}%".format(greatRate))






