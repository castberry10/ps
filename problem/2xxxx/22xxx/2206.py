import sys 
from collections import deque
import pprint
n, m = map(int, input().split())
mapdata = []

for _ in range(n):
    mapdata.append(list(sys.stdin.readline().rstrip()))

visit = [[[0] * 2 for _ in range(m)] for _ in range(n)]
xp = [1, -1, 0, 0]
yp = [0, 0, 1, -1]

queue = deque()
queue.append([0, 0, 0])
answer = -1
visit[0][0][0] = 1


# print(len(mapdata), len(mapdata[0]))
# pprint.pprint(mapdata)
def bfs():
    global n, m, answer
    while queue:
        y, x, c = queue.popleft() #세로, 가로, 찬스 .. ?
        # print(y, x, c, visit[y][x][c]) #debuging . . .
        if y == n - 1 and x == m - 1:
            answer = visit[y][x][c]
            return
        for i in range(4):
            dy = y + yp[i]
            dx = x + xp[i]
            
            if 0 <= dy < n and 0<= dx < m and visit[dy][dx][c] == 0:
                if mapdata[dy][dx] == '0':
                    visit[dy][dx][c] = visit[y][x][c] + 1
                    queue.append([dy, dx, c])
                if c == 0 and mapdata[dy][dx] == '1':
                    visit[dy][dx][1] = visit[y][x][0] + 1
                    queue.append([dy, dx, 1])
bfs()
print(answer)