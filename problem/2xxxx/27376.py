import sys
n, k = map(int, input().split())

sinho = {}
for _ in range(k):
    x, t, s = map(int, sys.stdin.readline().split())
    sinho[x] = (t, s)
sigan = 1
for i in range(1, n + 1):
    if i in 