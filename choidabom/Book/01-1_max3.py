# 세 정수를 입력받아 최댓값 구하기

print(' 세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요: '))
b = int(input('정수 b의 값을 입력하세요: '))
c = int(input('정수 c의 값을 입력하세요: '))

# a, b, c의 최댓값을 maximum으로 구하는 과정
# 순차 구조 sequential structure
maximum = a
if b > maximum : maximum = b
if c > maximum : maximum = c

print(f'최댓값은 {maximum}입니다.')

# -----------------------------
# 함수 이용
# max3() 함수는 매개변수 a, b, c에 숫자를 입력받아 최댓값을 구하여 반환한다.

def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum


# -----------------------------
# input() 함수는 키보드로 문자열을 반환한다. 
# input() 함수에 문자열을 전달하여 'input(문자열)'과 같이 호출됨.
# 문자열을 enter까지 입력해야 완료되지만 enter 출력 안 함.


name = input('이름을 입력하세요: ')
# print('이름을 입력하세요: ', end='')
# name=input()


print(f'안녕하세요? {name}님.')