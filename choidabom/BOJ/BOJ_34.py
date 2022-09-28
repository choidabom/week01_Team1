# 1181: 단어 정렬

# 알파벳 소문자로 이루어진 n개의 단어
# 1. 길이가 짧은 것부터
# 2. 길이가 같으면 사전 순으로

# import sys

# # sum()으로 2차원 리스트를 1차원 리스트로 변환
# word_list = sum(word_list, [])

# # 문자열의 길이 순으로 정렬
# word_list.sort(key=len)

import sys

N = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for i in range(N)]
result_list = [set() for _ in range(0, 52)]

for word in word_list:
    result_list[len(word)].add(word)

for result in result_list:
    # list.sorted(): 알파벳 순서로 문자열 정렬
    result = sorted(list(result))
    for res in result:
        print(res)

# 삽입정렬 => 알파벳 순으로 됨
# def insertion_sort(a):
#     n = len(a)
#     for i in range(0, n):
#         j = i
#         tmp = a[i]
#         while j > 0 and a[j-1] > tmp:
#             a[j] = a[j-1]
#             j -= 1
#         a[j] = tmp