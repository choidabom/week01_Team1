# 17478: 재귀함수가 뭔가요?
# JH 교수님이 만들 챗봇의 응답을 출력하는 프로그램
# "재귀함수가 뭔가요?" 0 4 8 12 등차로 _ 개수 생성

import sys
# 교수님이 출력을 원하는 재귀 횟수 N(1<=N<=50)
n = int(sys.stdin.readline())

def answer(x):
    print('____' * x, end="")
    print('"재귀함수가 뭔가요?"')
    print('____' * x, end="")
    print('"재귀함수는 자기 자신을 호출하는 함수라네"')

# n = 2
def recur_function(n):
    for i in range(0, n):
        print('____' * i, end="")
        print('"재귀함수가 뭔가요?"')
        print('____' * i, end="")
        print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____' * i, end="")
        print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____' * i, end="")
        print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        if (i+1) != n:
            continue
        elif (i+1)==n:
            answer(n)

    for j in range(n, -1, -1):
        print('____' * j, end="")
        print('라고 답변하였지.')


print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
recur_function(n)

# print문 끝에 None이 뜬 이유 => print문 안에 함수를 넣었기 때ㅜㅁㄴ인데
# 해당 함수의 리턴값을 정해놓지 않았기 때문이다.

# 입력과 출력
# 1
# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"재귀함수는 자기 자신을 호출하는 함수라네"
# ____라고 답변하였지.
# 라고 답변하였지.

# 2
# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________"재귀함수가 뭔가요?"
# ________"재귀함수는 자기 자신을 호출하는 함수라네"
# ________라고 답변하였지.
# ____라고 답변하였지.
# 라고 답변하였지.

# 3
# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________"재귀함수가 뭔가요?"
# ________"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ________마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ________그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____________"재귀함수가 뭔가요?"
# ____________"재귀함수는 자기 자신을 호출하는 함수라네"
# ____________라고 답변하였지.
# ________라고 답변하였지.
# ____라고 답변하였지.
# 라고 답변하였지.

# 4
# 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
# "재귀함수가 뭔가요?"
# "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# 그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____"재귀함수가 뭔가요?"
# ____"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________"재귀함수가 뭔가요?"
# ________"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ________마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ________그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ____________"재귀함수가 뭔가요?"
# ____________"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
# ____________마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
# ____________그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
# ________________"재귀함수가 뭔가요?"
# ________________"재귀함수는 자기 자신을 호출하는 함수라네"
# ________________라고 답변하였지.
# ____________라고 답변하였지.
# ________라고 답변하였지.
# ____라고 답변하였지.
# 라고 답변하였지.