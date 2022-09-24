# 1085: 직사각형에서 탈출

# 한수 위치 (x, y)
# 직사각형은 각 변이 좌표축에 평행하고, 
# 왼쪽 아래 꼭짓점은 (0, 0)
# 오른쪽 위 꼭짓점은 (w, h)
# 직사각형의 경계선까지 가는 거리의 최솟값을 구해라

# 입력 x, y, w, h

x, y, w, h = map(int, input().split())

# 경계선까지의 가는 최솟값을 구하면 되기 때문에
# 먼저 x, y, w-x, h-y 값을 비교하면 될 것 같다.

minimum = x

if x < y:
    minimum = x
    if x < w-x:
        minimum = x
        if x < h-y:
            minimum = x
        else:
            minimum = h-y
    else:
        minimum = w-x
        if w-x < h-y:
            minimum = w-x
        else:
            minimum = h-y

elif x > y:
    minimum = y
    if y < w-x:
        minimum = y
        if y < h-y:
            minimum = y
        else:
            minimum = h-y
    else:
        minimum = w-x
        if w-x < h-y:
            minimum = w-x
        else:
            minimum = h-y
    
print(minimum)