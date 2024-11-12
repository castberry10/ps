from collections import deque

move = [(-1, -1), (-1, 0), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    datamap = list()
    visitmap = [[0 for _ in range(w)] for _ in range(h)]
    answer = 0
    queue = deque()
    
    for i in range(h):
        datamap.append(list(map(int, input().split())))
    
    for i in range(h):
        for j in range(w):
            if datamap[i][j] == 1 and visitmap[i][j] == 0:
                queue.append((j , i))
            while len(queue) > 0:
                x, y = queue.popleft()
                # print(y, x, visitmap[y][x])
                if visitmap[y][x] == 0:
                    visitmap[y][x] = 1
                    answer += 1
                for dx, dy in move:
                    if 0 <= x + dx < w and 0 <= y + dy < h and visitmap[y+dy][x + dx] == 0 and datamap[y+dy][x + dx] == 1:
                        visitmap[y + dy][x + dx] = 1
                        queue.append((x+dx, y+ dy))

    print(answer)