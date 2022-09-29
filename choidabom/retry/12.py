import sys
n = int(sys.stdin.readline())
ox_list = [sys.stdin.readline().strip() for i in range(n)]

for i in range(n):
    count = 0
    sum_count = 0
    for j in range(len(ox_list[i])):
        if ox_list[i][j] == 'O':
            count = count + 1
            sum_count += count
        else:
            count = 0
    print(sum_count)


# 누적 증가 ....! ?