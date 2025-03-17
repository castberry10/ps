
import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

def solve():
    visit = [[0 for i in range(3)] for j in range(3)]
    data = []
    for _ in range(3):
        data.append(list(input().strip()))
    data2 = list(map(int, input().split()))
    n = data2[0] 
    answer = data2[1:] 
    
    def bfs(y, x, cnt):
        dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
        queue = deque()
        queue.append((y, x))
        visit[y][x] = cnt
        size = 1
        
        while queue:
            cy, cx = queue.popleft()
            for dy, dx in dxy:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < 3 and 0 <= nx < 3:
                    if data[ny][nx] == 'O' and visit[ny][nx] == 0:
                        queue.append((ny, nx))
                        visit[ny][nx] = cnt
                        size += 1
        return size
    
    cnt = 1
    sizes = []
    for i in range(3):
        for j in range(3):
            if data[i][j] == 'O' and visit[i][j] == 0:
                sizes.append(bfs(i, j, cnt))
                cnt += 1
    
    sizes.sort()
    
    if len(sizes) != len(answer):  
        print(0)
        return
    
    for i in range(len(sizes)):
        if sizes[i] != answer[i]:
            print(0)
            return
    
    print(1)

for i in range(t):
    solve()