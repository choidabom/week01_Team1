# 세 정수를 입력받아 중앙값 구하기 1

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('세 정수의 중앙값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.:'))
b = int(input('정수 b의 값을 입력하세요.:'))
c = int(input('정수 c의 값을 입력하세요.:'))

print(f'중앙값은 {med3(a, b, c)입니다.')

a b c

# 코드는 짧지만 비교를 마친 상태에서 다시 비교를 하는 경우가 생기기 때문에 효율이 좋지 x

def med3(a, b, c):
    # 중앙값이 a인 경우
    #  c <= a <= b 혹은 b <= a <= c
    if (b >= a and c <= a) or (b <= a and a <= c): return a
    
    # 중앙값이 b인 경우
    # a <= b <= c 혹은 c <= b <= a
    elif (a <= b and b <= c) or (c <= b and b <= a): return b

    # 중앙값이 c인 경우
    else: return c