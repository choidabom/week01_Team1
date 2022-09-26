# 10 ~ 99 사이의 난수 n개 생성하기(13이 나오면 중단)
# 난수 => 정의된 범위내에서 무작위로 추출된 수

import random

n = int(input('난수의 개수를 입력하세요.: '))

for i in range(n):
    # 난수 생성
    r = random.randint(10, 99)
    print(r , end=' ')
    if r == 13: 
        print('프로그램을 중단합니다.\n')
        break