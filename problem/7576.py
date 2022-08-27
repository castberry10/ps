#2차원 dfs    / / replit.com
from collections import deque
# append():- This function is used to insert the value in its argument to the right end of the deque.
# appendleft():- This function is used to insert the value in its argument to the left end of the deque.
# pop():- This function is used to delete an argument from the right end of the deque.
# popleft():- This function is used to delete an argument from the left end of the deque.
M, N = map(int, input().split())

box = []
# [[[1, 1], [1, 1]], [[2, 2], [2, 2]], [[3, 3], [3, 3]]]
# [y -> N][x - > M]
queue = deque()  #popleft, append

box= [list(map(int, input().split())) for _ in range(N)]
answer = 0
dxy = [(0, -1), (0, 1), (1, 0), (-1, 0), (0, 0), (0, 0)]
# 1 찾아서 큐에 넣기

for y in range(N):
    for x in range(M):
        if box[y][x] == 1:
            queue.append([y, x])
# 1 입력 끝 bfs 시작
#
while queue:
    y, x = queue.popleft()
    for i in range(6):
        dx, dy = dxy[i]
        if 0 <= dx + x < M and 0 <= dy + y < N:  #배열 오류 방지
            if box[y + dy][x + dx] == 0:
                box[y + dy][x + dx] += box[y][x] + 1
                queue.append([y + dy, x + dx])

#검증
ck = 1

for y in range(N):
    if ck == 0:
        break
    for x in range(M):
        if box[y][x] == 0:
            ck = 0
            break
        if box[y][x] > answer:
            answer = box[y][x]
    # print(box[0])
    # print(box[1])
# print(dxyh)
if ck == 0:
    print(-1)
else:
    print(answer - 1)

