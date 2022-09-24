# 11654: 아스키 코드

# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

import sys

inputs = sys.stdin.readline().strip()
# ord() 함수를 사용하여 아스키코드로 변환할 수 있다.
print(ord(inputs))