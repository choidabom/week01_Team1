import sys
sys.stdin = open(‘BOJ/input.txt’, ‘r’)
input = sys.stdin.readline
N, r, c = list(map(int, input().split()))
move = 0
# target = (r, c)
quadrants = []
def do_move(quadrants):
    sum = 0
    for idx in range(len(quadrants)):
        sum += quadrants[idx]*4**(N-1-idx)
    return sum
def get_quadrant(n):
    global c, r
    if n == 0:
        return
    else:
        x = c // 2**(n-1)
        y = r // 2**(n-1)
        if [x, y] == [0, 0]:
            quadrants.append(0)
        elif [x, y] == [1, 0]:
            quadrants.append(1)
        elif [x, y] == [0, 1]:
            quadrants.append(2)
        elif [x, y] == [1, 1]:
            quadrants.append(3)
        c %= 2**(n-1)
        r %= 2**(n-1)
        get_quadrant(n-1)
get_quadrant(N)
# print(quadrants)
print(do_move(quadrants))