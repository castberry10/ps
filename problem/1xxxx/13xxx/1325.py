from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = {}
for i in range(m):
    a, b = map(int, input().split())
    if b not in graph:
        graph[b] = []
    graph[b].append(a)
answer = []

# def bfs(n):
#     temp = 0
#     queue = deque()
#     queue.append(n)
#     visit = set()
#     visit.add(n)
#     while queue:
#         tempa = queue.popleft()
#         temp += 1
#         if tempa not in graph:
#             continue
#         for ia in graph[tempa]:
#             if ia not in visit:
#                 visit.add(ia)
#                 queue.append(ia)
#     return temp

maxcomputer = 0
answer = []

for i in graph:
    temp = 0
    queue = deque()
    queue.append(i)
    visit = set()
    visit.add(i)
    while queue:
        tempa = queue.popleft()
        temp += 1
        if tempa not in graph:
            continue
        for ia in graph[tempa]:
            if ia not in visit:
                visit.add(ia)
                queue.append(ia)
    # print(temp, maxcomputer)
    if maxcomputer < temp:
        maxcomputer = temp
        answer = [i]
        # print('maxcomputer > temp')
    elif maxcomputer == temp:
        answer.append(i)
        # print('maxcomputer == temp')
answer.sort()
print(*answer)