import sys, math

def main():
    n = int(sys.stdin.readline().strip())
    numbers = [sys.stdin.readline().strip() for i in range(n)]

    for i in range(n):
        number = int(numbers[i])
        halfPoint = math.ceil(number/2)
        for currentNumber in range(halfPoint, 1, -1):
            if checkSosu(currentNumber) == True:
                if checkSosu(number - currentNumber) == True:
                    print(currentNumber, number-currentNumber)
                    break

def checkSosu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

main()


##### 아래는 시간 초과된 코드 #####

# import sys, math

# n = int(sys.stdin.readline().strip())
# numbers = [sys.stdin.readline().strip() for i in range(n)]

# for i in range(n):
#     number = int(numbers[i])
#     array = [True for i in range(number)]
#     for j in range(2, len(array)):
#         if array[j] == True:
#             for k in range(2, j):
#                 if j%k == 0:
#                     for l in range(j, len(array), j):
#                         array[l] = False

#     halfPoint = math.ceil(number/2)
#     for pointer in range(halfPoint, 1, -1):
#         if array[pointer] == True:
#             if array[number - pointer] == True:
#                 print(pointer, number-pointer)
#                 break
