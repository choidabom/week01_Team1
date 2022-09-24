# 2577: 숫자의 개수

# 세 개의 자연수 A, B, C가 주어질 때 A*B*C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램 작성

A = int(input())
B = int(input())
C = int(input())

# list() 함수에 문자열을 넣으면 한 문자씩 다 나누어 리스트를 생성한다. (공백도 한 문자로 취급)
num = list(str(A*B*C))

# 전체 리스트에서 0부터 9까지 각각 몇 개가 있는지 카운팅 
print(num.count('0'))
print(num.count('1'))
print(num.count('2'))
print(num.count('3'))
print(num.count('4'))
print(num.count('5'))
print(num.count('6'))
print(num.count('7'))
print(num.count('8'))
print(num.count('9'))


