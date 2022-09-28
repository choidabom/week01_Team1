# 8958: OX 퀴즈

# O는 문제 맞음
# x는 문제 틀림
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수
import sys

Testcase = int(sys.stdin.readline().strip()) # 테스트 케이스의 개수

for _ in range(Testcase):
    array = input()
    score = 0
    sum_score = 0
    for ox in array:
        if ox == 'O':
            score = score + 1
            sum_score += score
        else:
            score = 0
    print(sum_score)

# 입력
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX

# 출력
# 10
# 9
# 7
# 55
# 30