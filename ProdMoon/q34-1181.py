import sys

n = int(sys.stdin.readline().strip())

words = ['0' for i in range(n)]
strStorage = [[] for i in range(51)]    # 이 리스트의 index값은 곧 문자열의 길이임.

for i in range(n):
    word = sys.stdin.readline().strip()
    strStorage[len(word)].append(word)

for i in range(51):
    strStorage[i].sort()
    if len(strStorage[i]) == 1:
        print(strStorage[i][0])
    else:
        temp = ""
        for j in range(len(strStorage[i])):
            if temp != strStorage[i][j]:
                print(strStorage[i][j])
                temp = strStorage[i][j]