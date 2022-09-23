import sys

def main():

    n = int(sys.stdin.readline().strip())

    if n < 100 :
        print(n)
    else:
        count = 99
        for i in range(100, n+1):
            if sameCheck(i) == True:
                count = count + 1
        print(count)
    

def sameCheck(num):
    array = list(str(num))
    minus = int(array[0]) - int(array[1])

    for i in range(len(array)-1):
        if minus != int(array[i]) - int(array[i+1]):
            return False
    return True


main()