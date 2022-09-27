import sys

n = int(sys.stdin.readline().strip())

dosuArr = [0] * 10001   # 도수 분포표의 길이 == 데이터의 범위 최대값 + 1

for i in range(n):
    inputVal = int(sys.stdin.readline().strip())
    dosuArr[inputVal] += 1

for i in range(len(dosuArr)):
    for j in range(0, dosuArr[i]):
        print(i)