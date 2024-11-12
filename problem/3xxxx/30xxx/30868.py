n = int(input())

for _ in range(n):
    a = int(input())
    while a > 4:
        a -= 5
        print('++++ ', end='')
    for i in range(a):
        print('|', end='')
        
    print()
        