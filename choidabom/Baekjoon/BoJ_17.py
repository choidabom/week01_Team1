# 2675: 문자열 반복

# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력

import sys
# 첫째 줄: 테스트 케이스의 개수 T
testCase = int(sys.stdin.readline())

# 각 테스트 케이스는 반복 횟수 R(1<=R<=8)
# 문자열 S가 공백으로 구분되어 주어짐
inputs = [sys.stdin.readline().split() for i in range(testCase)]


for i in range(testCase):
    # R: 각 테스트 케이스 반복 횟수
    R = int(inputs[i][0])
    S = list(inputs[i][1])

    for j in range(len(S)):
        print(S[j] * R, end="")
    print()