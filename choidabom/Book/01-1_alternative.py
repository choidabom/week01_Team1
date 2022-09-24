# 특정 문자를 줄바꿈 없이 연속으로 출력하는 프로그램
# +와 -를 번갈아가면서 출력하기

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇 개를 출력할까요?'))

for i in range(n):
    if i % 2:
        print('-', end='') # 홀수인 경우 - 출력
    else:
        print('+', end='') # 짝수인 경우 + 출력

print()

# 이 프로그램은 잘 작동하지만 효율성의 문제가 있다.
# for문 반복 n번, if문 반복 n번, 나눗셈 n번
# n이 50,000이라면 if문도 50,000 반복됨
