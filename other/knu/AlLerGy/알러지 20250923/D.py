from collections import deque

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
queue = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            queue.append((i, j))

mapping = [[-1] * m for _ in range(n)]
map_num = 1     
while queue:
    x, y = queue.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            queue.append((nx, ny))
