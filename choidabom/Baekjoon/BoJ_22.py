# 9020: 골드바흐의 추측
# 2보다 큰 짝수 n이 주어졌을 때, n의 골드바흐 파티션을 출력
# 가능한 n의 골드바흐 파티션이 여러가지인 경우 두 소수의 차이가 가장 작은 것을 출력

import sys

N = int(sys.stdin.readline()) 
num = [sys.stdin.readline().split() for i in range(N)]

for i in range(N):
    # print('테스트 케이스: ', int(num[i][0]))
    mok = int(int(num[i][0]) / 2)

    # 몫보다 작은 가장 가까운 소수 찾기

    for sosu in range(mok, 1, -1):
        tmp = True
        if sosu == 1:
            tmp = False
        for j in range(2, sosu):
            if sosu == 2 or sosu == 3:
                tmp = True
                break
            elif sosu % j == 0:
                tmp = False
                
        if tmp == True:
            namugi = int(num[i][0])-sosu
            # print('소수:', sosu)
            # print('소수 나머지:', namugi)
            
            for sosu2 in range(namugi, 1, -1):
                tmp2 = True
                if sosu2 == 1:
                    tmp2 = False
                for j in range(2, sosu2):
                    if sosu2 == 2 or sosu2 == 3:
                        tmp2 = True
                        break
                    elif sosu2 % j == 0:
                        tmp2 = False
                        
                if tmp2 == False:
                    sosu -= 1
                    break
                    
                else:
                    print(sosu, sosu2)
                    break
        if tmp == True and tmp2 == True:
            break
                
    

# 입력
# 3
# 8
# 10
# 16

# 출력
# 3 5
# 5 5
# 5 11