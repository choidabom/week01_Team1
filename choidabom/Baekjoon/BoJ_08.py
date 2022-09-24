# 10950: A + B -3

# 첫째 줄에 테스트 케이스의 개수 T
T = int(input())

# 두 정수 A와 B를 입력받은 다음, A+B 출력
for _ in range(T):
    A, B = map(int, input().split())
    print(A+B)    

# 준호오빠 코드
# caseNum = input()

# array = [0 for n in range(int(caseNum))]

# for i in range(int(caseNum)):
#     array[i] = list(input().split())

# for i in range(int(caseNum)):
#     result = int(array[i][0])+int(array[i][1])
#     print(result)