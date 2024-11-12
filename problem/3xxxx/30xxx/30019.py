import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

li = [0] * (n + 2)

for i in range(m):
    k, s, e = map(int, input().split())
    if s >= li[k]:
        print('YES')
        li[k] = e
    else:
        print('NO')