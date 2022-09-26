# 1 ~ 12까지 8을 건너뛰고 출력하기 1

# 단순히 리스트를 사용해서 8을 건너뜀
for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end= ' ')