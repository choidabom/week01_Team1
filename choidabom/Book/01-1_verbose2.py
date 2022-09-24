# a부터 b까지 정수의 합을 구하는 과정과 최종값 출력

import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

# 두 값 교환하기: 오름차순 정렬
if a > b:
    a, b = b, a

sum = 0
# 진행 중인 값: for문에서 a부터 b-1까지 값 뒤에 +를 붙여 출력
for i in range(a, b):
    print(f'{i} + ', end='')
    sum += i    # sum에 i를 더함

# 최종값: b의 값 뒤에 =를 붙여 출력
print(f'{b} = ', end='')
sum += b    #sum에 b를 더함

print(sum)