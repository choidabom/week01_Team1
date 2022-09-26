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
import sys

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

# 1978 소수 찾기 -- 에라토스테네스의 체
'''
import sys
N = sys.stdin.readline()
num_list = list(map(int, sys.stdin.readline().split()))
count = 0

for num in num_list:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
print(count)
'''

# 9020 골드바흐의 추측
'''
import sys

def check_sosu(num, check):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            check += 1
    return check


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    for i in range(int(n / 2), 0, -1):
        if i != 2 and i % 2 == 0:
            continue
        a = i
        b = n-i
        check = 0
        check = check_sosu(a, check)
        if check == 1:
            check = check_sosu(b, check)
        if check == 2:
            print(f"{a} {b}")
            break
'''

# 1065 한수
'''
import sys
X = int(sys.stdin.readline().strip())
count_answer = 0
for i in range(1, X+1):
    if i<=99:
        count_answer += 1
        continue
    str_i = str(i)
    str_list = [int(_) for _ in str_i]
    total_minus_list = []
    for j in range(len(str_list)-1):
        total_minus_list.append(str_list[j]-str_list[j+1])

    before_k = total_minus_list[0]
    for k in total_minus_list:
        if k != before_k:
            break
        before_k = k

    else:
        count_answer += 1
print(count_answer)
'''

# 2628 종이자르기 -- 코드 좀 더 깔끔하게
'''
import sys
X, Y = map(int, sys.stdin.readline().split())
width_list, height_list, width_num_list, height_num_list = [], [], [], []
for _ in range(int(sys.stdin.readline())):
    t, num = map(int, sys.stdin.readline().split())
    if t == 1:
        width_list.append(num)
    else:
        height_list.append(num)

width_list.sort()
height_list.sort()
if len(width_list) != 0:
    before_width = 0
    for width in width_list:
        width_num_list.append(width - before_width)
        before_width = width
    width_num_list.append(X-before_width)
else:
    width_num_list.append(X)

if len(height_list) != 0:
    before_height = 0
    for height in height_list:
        height_num_list.append(height - before_height)
        before_height = height
    height_num_list.append(Y - before_height)
else:
    height_num_list.append(Y)

result_list = []
for w in width_num_list:
    for h in height_num_list:
        result_list.append(w*h)
print(max(result_list))
'''

# 10872 팩토리얼 - 재귀형, 절차형
## 절차형
''' 
import sys
N = int(sys.stdin.readline())+1
result = 1
for i in range(1,N):
    result *= i
print(result)
'''

## 재귀형
'''
def factorial(n):
    if n == 1:
        return 1
    result = n * factorial(n-1)
    return result
    factorial(5)
'''

# 17478 재귀함수가 뭔가요? -- 역방향으로 나가야 한다.
'''
import sys
global N
N = int(sys.stdin.readline())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def create_sentence(n):
    if n==N:
        s1 = '"재귀함수가 뭔가요?"'
        s2 = '"재귀함수는 자기 자신을 호출하는 함수라네"'
        s3 = '라고 답변하였지.'
        s_list = [s1,s2,s3]
        for s in s_list:
            print("_"*n*4 + s)
        return None
    print('_'*n*4+'"재귀함수가 뭔가요?"')
    print('_'*n*4+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print('_' * n * 4 + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
    print('_' * n * 4 + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    create_sentence(n + 1)
    print('_' * n * 4 + '라고 답변하였지.')

create_sentence(0)
'''

# 5568 카드 놓기 -- 재귀, 순열 2가지 방식
## 재귀
'''
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card_list = []
dp = [0] * n
word = ''
result = set()


for _ in range(n):
    card_list.append(sys.stdin.readline().strip())


def check_recursion(cnt):
    global word

    if cnt == k:
        result.add(word)
        return

    for i in range(n):
        if dp[i] == 0:
            dp[i] = 1

            tmp = str(card_list[i])
            word += tmp

            check_recursion(cnt + 1)

            dp[i] = 0
            word = word[:-len(tmp)]


check_recursion(0)
print(len(result))
'''

## 순열
'''
import sys
from itertools import permutations

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

card_list = []
dp = [0] * n
word = ''
result = set()

for _ in range(n):
    card_list.append(sys.stdin.readline().strip())
for per in permutations(card_list, k):
    result.add(''.join(per))
print(len(result))
'''

# 1914 하노이 탑
'''
import sys
N = int(sys.stdin.readline())

def f(n, a, b, c):
    if (n == 1):
        print(a, c, sep = " ")
    else:
        f(n-1, a, c, b)
        f(1, a, b, c)
        f(n-1, b, a, c)

print(2**N-1)

if (N <=20):
    f(N, 1, 2, 3)
'''

# 9663 N-Queen
import sys

N = int(sys.stdin.readline())

board = [[0]*N for _ in range(N)]

result = 0
count = 0

def print_cb(board):
    for b in board:
        print(b)

def fill_straight(board, x, y):
    board[y] = [1] * N
    for i in range(N):
        board[i][x] = 1
    return board


def fill_diagnal(board, x, y):
    # / 방향
    down_right_base = x+y
    i = 0
    while (i + x) <= N-1 and (i+y) <= N-1:
        print(down_right_base-i, i)
        board[down_right_base-i][i] = 1
        board[i][down_right_base - i] = 1
        i+=1
    # i = 0
    # while 0<=i<=(N-1) and 0<=down_right_base-i<=(N-1):
    #     board[i][down_right_base-i] = 1
    #     i += 1
    # \ 방향
    tmp_x = x - min(x, y)
    tmp_y = y - min(x, y)
    while (tmp_x <= N-1) and (tmp_y <= N-1):
        board[tmp_y][tmp_x] = 1
        tmp_x += 1
        tmp_y += 1
    return board
print_cb(fill_diagnal(board, 0,4))








#
# def queen(n, board):
#     if count == N:
#         return
#
#     w = n % N
#     h = n // N
#
#     print(n, w, h)
#     if board[w][h] == 0:
#         count += 1
#
#     board[w] = [1]*N
#
#
#     for i in range(N):
#         board[i][h] = 1
#
#     queen(n - 1, board)
#
# queen(N*N - 1, board)

# 2750 수 정렬하기
## 소스코드
'''
N = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for num in num_list:
    print(num)
'''
## 버블정렬

'''
N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))

for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

for n in M:
    print(n)
'''

## 삽입정렬
'''
N = int(sys.stdin.readline())
M = []

for _ in range(N):
    M.append(int(sys.stdin.readline()))

for i in range(1, len(M)):
    while (i > 0) & (M[i] < M[i-1]):
        M[i], M[i-1] = M[i-1], M[i],

        i -= 1
for n in M:
    print(n)
'''

## 합병정렬

# 2751 수 정렬하기2
'''
import sys
N = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for num in num_list:
    print(num)
'''

# 10989 수 정렬하기3
'''
import sys
N = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(N):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
'''

## quick sort
'''
import sys
N = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[(len(arr) // 2)]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

result = quick_sort(num_list)

for res in result:
    print(res)
'''

# 1181 단어정렬
'''
import sys

N = int(sys.stdin.readline())
word_list = []
result_list = [set() for _ in range(0, 52)]

for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.append(word)

for word in word_list:
    result_list[len(word)].add(word)

for result in result_list:
    result = sorted(list(result))
    for res in result:
        print(res)
'''


# 2309 일곱 난쟁이
'''
import sys
height_list = [int(sys.stdin.readline()) for _ in range(9)]

total_height = sum(height_list)
finish = 0
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if total_height-(height_list[i] + height_list[j]) == 100:
            del height_list[i]
            del height_list[j-1]
            finish = 1
            break
    if finish == 1:
        break

height_list.sort()
for height in height_list:
    print(height)
'''

# 2798 블랙잭
'''
import sys
N, M = map(int, sys.stdin.readline().split())

card_list = list(map(int, sys.stdin.readline().split()))
best_score = 0
best_score_diff = 300000000
for i in range(N):
    for j in range(N):
        for k in range(N):
            if i == j or j == k or i == k:
                pass
            else:
                now_score = card_list[i] + card_list[j] + card_list[k]
                now_score_diff = M - now_score
                if 0 <= now_score_diff <= best_score_diff:
                    best_score_diff = now_score_diff
                    best_score = now_score
print(best_score)
'''

# 10819 차이를 최대로
## permutations
'''
import sys
from itertools import permutations

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

per = permutations(num_list)
answer =0

for i in per:
    s = 0
    for j in range(len(i) -1):
        s += abs(i[j] - i[j+1])
    if s > answer:
        answer = s
print(answer)
'''

# 10971 외판원 순회2 -- 순열 직접 구현해 보기
'''
import sys
from itertools import permutations
N = int(sys.stdin.readline())
city_list = [_ for _ in range(N)]
cost_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
per = permutations(city_list)
low_cost = 3000000

for p in per:
    cost = 0
    for i in range(N-1):
        tmp_cost = cost_list[p[i]][p[i+1]]
        if tmp_cost == 0:
            break
        else:
            cost += tmp_cost
    else:
        tmp_cost = cost_list[p[i+1]][p[0]]
        cost += tmp_cost
        if tmp_cost != 0 and cost <= low_cost:
            low_cost = cost

print(low_cost)
'''

# # 14888 연산자 끼워넣기
## 앞에 수도 섞을경우(잘못풀음)
'''
import sys
from itertools import permutations

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
oper_tmp_list = list(map(int, sys.stdin.readline().split()))

operator_list = []

for i in range(4):
    if i == 0:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('+')
    elif i == 1:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('-')
    elif i == 2:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('*')
    elif i == 3:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('//')


num_per = permutations(num_list)
operator_per = list(set(permutations(operator_list)))


def custom_oper_func(a,b, oper):
    if oper == '+':
        print(f'{a}+{b} = {a+b}')
        return a + b
    elif oper == '-':
        print(f'{a}-{b} = {a - b}')
        return a - b
    elif oper == '*':
        print(f'{a}*{b} = {a * b}')
        return a * b
    elif oper == '//':
        print(f'{a}//{b} = {custom_div(a,b)}')
        return custom_div(a,b)


def custom_div(a,b):
    if a > 0:
        return a // b
    elif a == 0:
        return 0
    elif a < 0:
        return -(-a // b)

result_list = []
for n_p in num_per:
    for o_p in operator_per:
        print("------------------")
        print(n_p)
        print(o_p)
        result = n_p[0]
        for i in range(N-1):
            result = custom_oper_func(result, n_p[i + 1], o_p[i])
        result_list.append(result)
print(max(result_list))
print(min(result_list))
'''

## 정상 풀이
'''
import sys
from itertools import permutations

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
oper_tmp_list = list(map(int, sys.stdin.readline().split()))

operator_list = []

for i in range(4):
    if i == 0:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('+')
    elif i == 1:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('-')
    elif i == 2:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('*')
    elif i == 3:
        for _ in range(oper_tmp_list[i]):
            operator_list.append('//')

operator_per = list(set(permutations(operator_list)))

def custom_oper_func(a,b, oper):
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '//':
        return custom_div(a,b)


def custom_div(a,b):
    if a > 0:
        return a // b
    elif a == 0:
        return 0
    elif a < 0:
        return -(-a // b)

result_list = []
for o_p in operator_per:
    result = num_list[0]
    for i in range(N-1):
        result = custom_oper_func(result, num_list[i + 1], o_p[i])
    result_list.append(result)
print(max(result_list))
print(min(result_list))
'''

