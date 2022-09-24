# 10869: 사칙연산

# 두 수를 사용자로부터 입력받고, 두 수에 대한 사칙연산을 모두 하여 출력하는 문제
# 두 자연수 A, B가 주어지는 것이니깐 입력하는 input 넣어줌.

A, B = input().split()
A = int(A)
B = int(B)

# A, B = map(int, input().split())
# map에 int와 input().split()을 넣으면 split의 결과를 모두 int로 변환해준다. 

# 파이썬은 print안에 여러 개 넣어도 됨.
print(A+B, A-B, A*B, int(A/B), A%B)