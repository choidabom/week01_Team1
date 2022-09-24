# 반복 과정에서 조건 판단하기
# *를 n개 출력하되 w개마다 줄바꿈하는 프로그램

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))
w = int(input('몇 개마다 줄바꿈할까요?: '))

# *를 n//w 번 출력하기
for _ in range(n//w):
    print('*'*w)

# *를 n%w번 출력 후 줄바꿈하기
# n이 w의 배수가 아닌 경우 마지막 행을 출력
rest = n % w
if rest:
    print('*'*rest)