while True:
    a = input()
    if a == '0':
        break
    while True:
        if len(a) == 1:
            print(a)
            break
        b = sum(map(int, tuple(a)))
        a = str(b)
    