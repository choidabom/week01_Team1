import sys
a = int(sys.stdin.readline())
# strip() 이용해서  '\n' 제거
b = sys.stdin.readline().strip() 
sum = 0 # 초기화 안 해주면 에러납니다~

for i in range(len(b)):
    # b[0]에서부터 시작이 아니기 때문에 잘 생각해야한다.
    each_b = int(b[len(b)-i-1])
    stage = int(a * each_b)
    print(stage)
    stage *= 10**i
    sum += stage
print(sum)
