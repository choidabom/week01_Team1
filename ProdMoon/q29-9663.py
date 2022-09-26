import sys

n = int(sys.stdin.readline().strip())

chessBoard = [0] * n
flag_row = [False] * n
flag_rightup = [False] * (2*n-1)
flag_rightdown = [False] * (2*n-1)

global count
count = 0

def nQueen(i):
    global count
    for j in range(n):
        if (
            flag_row[j] == False and
            flag_rightup[i+j] == False and
            flag_rightdown[j-i+(n-1)] == False
        ):
            chessBoard[i] = j
        
            if i == n-1:
                count = count + 1

            else:
                flag_row[j] = True
                flag_rightup[i+j] = True
                flag_rightdown[j-i+(n-1)] = True
                nQueen(i+1)
                flag_row[j] = False
                flag_rightup[i+j] = False
                flag_rightdown[j-i+(n-1)] = False


nQueen(0)
print(count)




##### 망한 코드 #####


# import sys, copy

# global count
# count = 0

# def nQueen(n, chessBoard):
#     global count
#     length = len(chessBoard)

#     if n == 1:
#         for row in chessBoard:
#             for area in row:
#                 if area == True:
#                     count = count + 1
#     else:
#         for i in range(length):
#             for j in range(length):
#                 copyBoard = copy.deepcopy(chessBoard)
#                 if copyBoard[i][j] == True:
#                     # 퀸의 경로에 False 넣는 작업 시작
#                     for k in range(length):
#                         copyBoard[i][k] = False
#                     for k in range(length):
#                         copyBoard[k][j] = False

#                     a = i
#                     b = j
#                     while a != -1 and b != -1:
#                         copyBoard[a][b] = False
#                         a = a - 1
#                         b = b - 1

#                     a = i
#                     b = j
#                     while a != length and b != length:
#                         copyBoard[a][b] = False
#                         a = a + 1
#                         b = b + 1

#                     a = i
#                     b = j
#                     while a != -1 and b != length:
#                         copyBoard[a][b] = False
#                         a = a - 1
#                         b = b + 1

#                     a = i
#                     b = j 
#                     while a != length and b != -1:
#                         copyBoard[a][b] = False
#                         a = a + 1
#                         b = b - 1
#                     # 작업 끝
                    
#                     nQueen(n-1, copyBoard)


# n = int(sys.stdin.readline().strip())

# chessBoard = [[True for i in range(n)] for i in range(n)]

# copyBoard = copy.deepcopy(chessBoard)
# nQueen(n, copyBoard)

# print(count)