# 32353
import sys
from collections import deque
input = sys.stdin.readline
h, w, r1, c1, r2, c2 = map(int, input.split())
apple_list = list()
mapdata = []
for i in range(h):
    mapdata.append(list(map(int, input().split())))
for i in range(w):
    p, q = map(int, input().split())
    apple_list.append([p,q])

# 위 1 오른쪽 2 아래 3 왼쪽 4 
if r2-r1 == 0:
    if c2 - c1 == -1:
        pass
    else:
        pass 
else:
    if r2 - r1 == -1:
        pass
    else:
        pass
state = 1
while True:
    