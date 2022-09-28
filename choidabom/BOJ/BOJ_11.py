# 2562: 최댓값

# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램

# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.


# 여러 줄 입력받아 배열로 저장
array = [map(int, input().split()) for _ in range(9)]

array = []
for _ in range(9):
    array.append(int(input()))

# max, min 메서드 존재 ~!
print(max(array))
# # index 함수도 존재 ~!
print(array.index(max(array))+1)

# 입력
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61

# 출력
# 85
# 8

