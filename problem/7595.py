while True:
    a = int(input())
    if a == 0:
        break
    for i in range(a):
        for j in range(i + 1):
            print('*', end = '')
        print()