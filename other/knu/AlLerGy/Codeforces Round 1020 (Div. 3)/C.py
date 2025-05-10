from itertools import permutations

def solve():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt = 0
    
    tof = False
    k = 0 
    for i in range(n):
        if b[i] == -1:
            cnt += 1
        else:
            if not tof:
                k = a[i] + b[i]
                tof = True
            else:
                if a[i] + b[i] != k:
                    print(0)
                    return
    mina = min(a)
    maxa = max(a)
    if tof:
        if k - maxa < 0 or k - mina > x:
            print(0)
        else:
            print(1)
    else:
        maxmmina = maxa - mina
        print(x - maxmmina + 1)
    

t = int(input())
for T in range(t):
    solve()