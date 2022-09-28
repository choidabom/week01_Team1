# 5568: 카드 놓기

# 상근이 => 카드 n(4<=n<=10)장 갖고 놀고 있음, 각 카드 1<=num<=99 정수
# n 중 k(2<=k<=4)장 선택, 가로로 나란히 정수 만듬
# 상근이가 만들 수 있는 정수는 모두 몇 가지?

import sys
import itertools
import functools
import operator

# n장의 카드
n = int(sys.stdin.readline())
# k개 선택
k = int(sys.stdin.readline())
# n장 나열
testCase = [sys.stdin.readline().split() for i in range(n)]

# print(testCase)
nPr = itertools.permutations(testCase, k)
nPr = list(nPr)
# print(nPr)

num_list = []
for i in range(len(nPr)):
    str1 = functools.reduce(operator.add, (nPr[i]))
    str2 = "".join(str1)
    num_list.append(str2)
print(len(set(num_list)))

# print(len(set(num_list)))