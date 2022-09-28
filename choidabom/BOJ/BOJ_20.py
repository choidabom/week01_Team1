# 2869: 달팽이는 올라가고 싶다

# 나무 막대 높이: V미터
# 낮: A미터 +
# 밤: B미터 -
# 정상에 올라간 후에 미끄러지지 x

import sys
import math

A, B, V = map(int, sys.stdin.readline().split())
 
# 마지막에 도착하는 과정에서 올라가는 것(+A) 빼고는 이미 나온 날짜
# 올라가면서 (+A) 하루 카운트 => + 1

days = math.ceil((V-A)/(A-B)) + 1

print(days)v