import sys
n, m = map(int, input().split())
r, c = 0, 0
garo = [0] * m
sero = [0] * n

for i in range(n-1):
    sero[i] = int(sys.stdin.readline())

garo = list(map(int, input().split()))

sero[n-1] = garo[0]

print(sero.index(min(sero)) + 1, garo.index(min(garo)) + 1)