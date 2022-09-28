# 10871: X보다 작은 수

# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램

# 정수 N개(로 이루어진 수열 A), 정수 X
N, X = map(int, input().split())

# 수열 A를 이루는 정수 N개
# 한 줄로 입력받은 값을 각 변수에 나누어 저장
array = list(map(int, input().split()))

for i in range(N):
    if array[i] < X:
        print(array[i], end=" ")
        # end = " "로 한 칸씩 띄어서 출력

# 입력
# 10 5
# 1 10 4 9 2 3 8 5 7 6

# 출력
# 1 4 2 3