import sys

n, r, c = list(map(int, sys.stdin.readline().split()))

def zzz(n, r, c, startPoint):
    if n == 1:
        print(int(startPoint + 2*r + c))

    else:
        if (
            (2**n)/(r+1) >= 2 and
            (2**n)/(c+1) >= 2
        ):
            zzz(n-1, r, c, startPoint)

        elif (
            (2**n)/(r+1) >= 2 and
            (2**n)/(c+1) < 2
        ):
            zzz(n-1, r, c-(2**n)/2, startPoint+ (2**(n-2))*(2**n))
        
        elif (
            (2**n)/(r+1) < 2 and
            (2**n)/(c+1) >= 2
        ):
            zzz(n-1, r-(2**n)/2, c, startPoint+ 2*(2**(n-2))*(2**n))
        
        else:
            zzz(n-1, r-(2**n)/2, c-(2**n)/2, startPoint+ 3*(2**(n-2))*(2**n))

zzz(n, r, c, 0)