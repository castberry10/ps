import sys
input = sys.stdin.readline
n, m, q = map(int, input().split())
mdata = [0] * m
ndata = [0] * n

for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        ndata[b] += c
    else:
        b -= 1
        mdata[b] += c
        
for i in range(n):
    for j in range(m):
        print(ndata[i] + mdata[j], end=" ")
    print()
    