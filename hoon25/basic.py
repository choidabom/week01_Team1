# -*- coding: utf-8 -*-
# 10869 사칙연산
'''
import sys
a, b = map(int, sys.stdin.readline().split())

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a % b)
'''

# 2588 곱셈
'''

import sys

data = list(map(lambda s: s.strip(), sys.stdin.readlines()))
a = int(data[0])
b = data[1][::-1]
for st in b:
    print(a*int(st))
print(a * int(data[1]))

# 숏코딩
a,b=map(int,open(0))
print(b%10*a,b%100//10*a,b//100*a,b*a)
'''

# 9498 시험성적
'''
import sys
data = int(sys.stdin.readline())

if data >= 90:
    print("A")
elif data >= 80:
    print("B")
elif data >= 70:
    print("C")
elif data >= 60:
    print("D")
else:
    print("F")
'''

# 2753 윤년  -> && , & , ||, | 의 차이
'''
import sys

data = int(sys.stdin.readline())
if (data % 4 == 0) & ((data % 100 != 0) | (data % 400 == 0)):
    print(1)
else:
    print(0)
'''

# 1085 직사각형에서 탈출
'''
import sys

x, y, w, h = map(int, sys.stdin.readline().split())
print(min(x, y, w-x, h-y))
'''

# 2739 구구단
'''
import sys

N = int(sys.stdin.readline())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}") 
'''

# 10950 A+B-3
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    x,y = map(int, sys.stdin.readline().split())
    print(x+y)
'''

# 2438 별찍기
'''
import sys
N = int(sys.stdin.readline())
for i in range(1,N+1):
    print('*'*i)
'''

# 10871 X보다 작은 수
'''
import sys

N, X = map(int,sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
for i in A:
    if i < X:
        print(i, end=' ')
'''

# 2562 최댓값
'''
import sys

A = list(map(lambda s: int(s.strip()), sys.stdin.readlines()))
big = 0
big_index = 0
for i, num in enumerate(A):
    if num > big:
        big = num
        big_index = i+1
print(big)
print(big_index)
'''

# 8958 OX퀴즈
'''
import sys
data = sys.stdin.readline()

total_score = 0
score = 0
for dt in data:
    if dt == 'O':
        score += 1
    else:
        score = 0
    total_score += score
print(total_score)
'''

# 4344 평균은 넘겠지
'''
import sys
for _ in range(int(sys.stdin.readline())):
    data = list(map(int,sys.stdin.readline().split()))
    N = data[0]
    del data[0]
    avg = sum(data)/N
    num = 0
    for score in data:
        if score> avg:
            num+=1
    print("%0.3f%%" % (round((num / N * 100), 3))) 
'''

# 2577 숫자의 개수
'''
import sys

A, B, C = map(lambda s: int(s.strip()), sys.stdin.readlines())
result = str(A * B * C)

result_dict = []
for i in range(10):
    result_dict[str(i)] = 0

for res in result:
    result_dict[res] += 1

for i in range(10):
    print(result_dict[str(i)])




import sys
import collections

A, B, C = map(lambda s: int(s.strip()), sys.stdin.readlines())
result = str(A * B * C)

result_dict = collections.OrderedDict()
for i in range(10):
    result_dict[str(i)] = 0

for res in result:
    result_dict[res] += 1

for answer in result_dict.values():
    print(answer)
'''

# 15596 정수의 개수 - type safe
'''
def solve(a :list) ->int:
    return sum(a)
'''

# 11654 아스키 코드
'''
import sys

C = sys.stdin.readline().strip()
print(ord(C))
'''

# 2675 문자열반복
'''
import sys

for _ in range(int(sys.stdin.readline())):
    cnt, word = sys.stdin.readline().split()
    for x in word:
        print(x*int(cnt), end='')
    print()
'''

# 1152 단어의 개수 -- split(' ') 와 split()의 차이
'''
import sys

sentence = sys.stdin.readline().strip()
print(len(sentence.split()))
'''

# 2908 상수
'''
import sys
num1, num2 = map(str, sys.stdin.readline().split())
print(max(int(num1[::-1]), int(num2[::-1])))
'''

# 2869 달팽이는 올라가고 싶다
'''
import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
if V >= A:
    print(math.ceil((V-A) / (A-B))+1)
else:
    print(1)
'''

# 1978 소수 찾기
import sys
N = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
count = 0

for num in num_list:
    if num == 1 or num == 2:
        continue
    div_num = num - 1
    while div_num >= 2:
        if (num % div_num) == 0:
            break
        div_num -= 1
    else:
        count += 1
print(count)







