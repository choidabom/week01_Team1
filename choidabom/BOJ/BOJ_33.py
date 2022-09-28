# 10989: 수 정렬하기 3

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

import sys
input = sys.stdin.readline
count_array = [0 for _ in range(10001)]
N = int(input())
for _ in range(N):
    number = int(input())
    count_array[number] += 1

for idx in range(len(count_array)):
    for _ in range(count_array[idx]):
        print(idx)