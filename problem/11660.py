import sys
n, m = map(int, input().split())
data = []
ps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
# 1 2    0 0 0
# 3 4    0 1 3
#        0 4 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps = data[]
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())