n = int(input())
for i in range(n):
    data = input()
    a = 0
    b = 0
    c = -1
    for d in data:
        if d == "0":
            c = 0
        elif d == "1":
            c = 1
        if d == "!":
            if c == -1:
                a += 1
            else:
                b += 1
    # print(a, b, c)
    if b > 0:
        c = 1
    if a % 2 == 0:
        print(c)
    else:
        if c == 1:
            print(0)
        if c == 0:
            print(1) 