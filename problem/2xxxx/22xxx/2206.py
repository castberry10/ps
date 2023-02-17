import sys 
n, m = map(int, input().split())
mapdata = []
for _ in range(n):
    mapdata.append(list(map(int, sys.stdin.readline().split())))
