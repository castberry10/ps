import sys 
input = sys.stdin.readline

def ck(p, s, a, k, n):
    total = 0  
    tof = False
    
    for i in range(n):
        if s[i] == 'R' and a[i] > p:
            if tof: 
                total += 1
            tof = False  
        else:
            if s[i] == 'B' and a[i] > p:
                if not tof:  
                    tof = True
    if tof:
        total += 1
    return total <= k

def solve(n, k, s, a):
    l = 0
    h = 10**9
    
    while l < h:
        m = (l + h) // 2
        if ck(m, s, a, k, n):
            h = m  
        else:
            l = m + 1  
    
    return l

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    a = list(map(int, input().split()))
    print(solve(n, k, s, a))
    