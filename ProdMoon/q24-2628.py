import sys

fullPaper = sys.stdin.readline().split() # 전체 종이 크기 입력받음 (가로 세로 순)
paperWidth = [0, fullPaper[0]] # 초기값 설정
paperHeight = [0, fullPaper[1]]

testCase = int(sys.stdin.readline().strip())

cutInfo = [] # [자르는 방향, 위치값], [자르는 방향, 위치값], ... (가로==0, 세로==1)

for i in range(testCase):
    cutInfo.append(sys.stdin.readline().split())

for info in cutInfo:
    if info[0] == '0':
        paperHeight.append(info[1])
    else:
        paperWidth.append(info[1])

paperWidth = list(map(int, paperWidth))
paperHeight = list(map(int, paperHeight))

paperWidth.sort()
paperHeight.sort()

longestWidth = 0
longestHeight = 0

for i in range(1, len(paperWidth)):
    temp = paperWidth[i] - paperWidth[i-1]
    if temp > longestWidth:
        longestWidth = temp

for i in range(1, len(paperHeight)):
    temp = paperHeight[i] - paperHeight[i-1]
    if temp > longestHeight:
        longestHeight = temp

print(longestWidth * longestHeight)





##### 아래는 망한 방법임 #####


# import sys

# def main():
#     fullPaper = sys.stdin.readline().split() # 전체 종이 크기 입력받음 (가로 세로 순)
#     paperLength = [[0, fullPaper[0]], [0, fullPaper[1]]] # 초기값 설정

#     testCase = int(sys.stdin.readline().strip())

#     cutInfo = [] # [자르는 방향, 위치값], [자르는 방향, 위치값], ... (가로==0, 세로==1)

#     for i in range(testCase):
#         cutInfo.append(sys.stdin.readline().split())

#     for i in range(testCase):
#         if cutInfo[i][0] == '0':
#             result = compare(paperLength[1], cutInfo[i][1])
#             if result[0] == 'cutLeft':
#                 paperLength[1][0] = result[1]
#             elif result[0] == 'cutRight':
#                 paperLength[1][1] = result[1]
#             else:
#                 pass

#         elif cutInfo[i][0] == '1':
#             result = compare(paperLength[0], cutInfo[i][1])
#             if result[0] == 'cutLeft':
#                 paperLength[0][0] = result[1]
#             elif result[0] == 'cutRight':
#                 paperLength[0][1] = result[1]
#             else:
#                 pass

#         else:
#             print('wrong cutting direction')
#             break
        

#     paperArea = (int(paperLength[0][1]) - int(paperLength[0][0])) * (int(paperLength[1][1]) - int(paperLength[1][0]))
#     print(paperArea)




# def compare(lengthArray, cutInfo):
#     temp_a = int(cutInfo) - int(lengthArray[0])
#     temp_b = int(lengthArray[1]) - int(cutInfo)
#     if temp_a <= temp_b:
#         if temp_a <= 0:
#             return 'pass', 0
#         else:
#             return 'cutLeft', temp_a
#     else:
#         if temp_b <= 0:
#             return 'pass', 0
#         else:
#             return 'cutRight', temp_b



# main()