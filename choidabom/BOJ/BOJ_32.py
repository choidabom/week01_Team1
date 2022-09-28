# 2751: 수 정렬하기 2

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for i in range(n)]

num.sort()  
for i in num:
    print(i)