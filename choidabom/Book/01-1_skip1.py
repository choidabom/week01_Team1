# 1 ~ 12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')

# 비효율적
# 예를 들어 숫자를 100,000까지 출력해야하는 경우 
# 숫자를 딱 1개 건너 뛸 경우 10만번을 판단해야하기 때문이다.