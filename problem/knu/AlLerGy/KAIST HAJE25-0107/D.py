import sys
from collections import deque
input = sys.stdin.readline
h, w, r1, c1, r2, c2 = map(int, input.split())
mapdata = []
for i in range(h):
    mapdata.append(list(map(int, input().split())))