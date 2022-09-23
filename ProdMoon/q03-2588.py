a = int(input())
b = int(input())

temp = list(str(b))

for i in range(2, -1, -1):
    print(int(temp[i]) * a)

print(a*b)