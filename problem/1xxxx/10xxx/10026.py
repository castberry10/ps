from collections import deque
colormap = []

n = int(input())
colorless_visit = [[0 for _ in range(n)] for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]

colorless_answer = 0
answer = 0 

queue = deque()

for i in range(n):
    colormap.append(list(input()))
    
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    for j in range(n):
        if visit[i][j] != 0:
            continue
        queue.append((i,j))
        visit[i][j] = 1
        answer += 1
        while True:
            if len(queue) == 0:
                break
            else:
                y, x = queue.popleft()
                state = colormap[y][x]
                for dy, dx in move:
                    if 0 <= y + dy < n and 0<= x + dx < n:
                        if state == colormap[y+dy][x+dx] and visit[y+dy][x+dx] == 0:
                            visit[y+dy][x+dx] = 1
                            queue.append((y+dy, x+dx))
for i in range(n):
    for j in range(n):
        if colorless_visit[i][j] != 0:
            continue
        queue.append((i,j))
        colorless_visit[i][j] = 1
        colorless_answer += 1
        while True:
            if len(queue) == 0:
                break
            else:
                y, x = queue.popleft()
                state = colormap[y][x]
                for dy, dx in move:
                    if 0 <= y + dy < n and 0<= x + dx < n:
                        if (state == colormap[y+dy][x+dx] or (state == 'R' and colormap[y+dy][x+dx] == 'G') or (state == 'G' and colormap[y+dy][x+dx] == 'R')) and colorless_visit[y+dy][x+dx] == 0:
                            colorless_visit[y+dy][x+dx] = 1
                            queue.append((y+dy, x+dx))
print(answer, end = ' ')
print(colorless_answer)
                    