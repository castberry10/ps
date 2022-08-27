from collections import deque

n, m = map(int, input().split())
map1 = [list(map(int, input())) for _ in range(n)]

dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]
queue = deque()
answer = 0
queue.append((0, 0))

map1[0][0] = 2
def dfs():
    while queue:
        y,x = queue.popleft()
        for i in range(4):
            dy, dx = dxy[i]
            # print(dy + y, dx + x)
            if 0 <= dx + x < m and 0 <= dy + y < n:
                # print(dy + y, dx + x)
                if map1[dy + y][dx + x] == 1:
                    queue.append((dy + y, dx + x))
                    # print(dy + y, dx + x)
                    map1[dy + y][dx + x] = map1[y][x] + 1


dfs()
# print(map1)
# for i in map1:      
#     for j in i:    
#         print(j, end=' ')
#     print()
print(map1[n -1 ][m -1 ])