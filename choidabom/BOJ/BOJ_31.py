# 2750: 수 정렬하기

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬

import sys
num = int(sys.stdin.readline())
x = [int(sys.stdin.readline()) for i in range(num)]

# sort() 메서드를 사용하면 빠르게 풀 수 있다.
# num.sort()  


# sort() 안 쓰고 풀어보기
# 단순 삽입 정렬 알고리즘
def insertion_sort(a):
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp

insertion_sort(x)

for i in range(num):
    print(x[i])
    

# 입력
# 5
# 5
# 2
# 3
# 4
# 1

# 출력
# 1
# 2
# 3
# 4
# 5

