import sys
input = sys.stdin.readline
t = int(input())

def solve():
    n = int(input())
    s = input().strip()

    d = s.count('-') 
    u = s.count('_')  

    if d < 2 or u < 1 or n < 3:
        print(0)
        return

    a = d // 2 
    b = d - a 
    print(a * b * u)

for i in range(t):
    solve()