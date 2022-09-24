# 2588: 곱셈

# 창훈오빠가 짠 코드
import sys

# 입력이 여러 줄로 들어왔을 때
data = list(map(lambda s: s.strip(), sys.stdin.readlines()))

a = int(data[0])
b = data[1][::-1]

for st in b:
    print(a*int(st))

print(a * int(data[1]))
