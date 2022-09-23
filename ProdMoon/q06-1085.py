data = input().split()

x = int(data[0])
y = int(data[1])
w = int(data[2])
h = int(data[3])

to_w = w - x
to_h = h - y

if x < to_w:
    w_short = x
else:
    w_short = to_w

if y < to_h:
    h_short = y
else:
    h_short = to_h

if w_short < h_short:
    print(w_short)
else:
    print(h_short)