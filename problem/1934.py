T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    sa, sb = a, b
    if b > a:
        a, b = b, a
    while True:
        if a % b ==0:
            break
        else:
            a, b = b, a % b
            
    print(sa * sb // b)
        