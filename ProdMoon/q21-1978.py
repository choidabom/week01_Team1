import sys

n = int(sys.stdin.readline().strip())
numbers = sys.stdin.readline().split()

sum = 0

for i in range(n):
    check = True
    if int(numbers[i]) == 1 :
        check = False
    else :
        j = 2
        while j*j <= int(numbers[i]) and check == True:
            if int(numbers[i])%j == 0 :
                check = False
            j = j + 1

    if check == True:
        sum = sum + 1

print(sum)