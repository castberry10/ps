import sys 
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

indegree = [0] * n
grape = {}
for i in range(m):
    a, b = map(int, input().split())
    if a - 1 not in grape:
        grape[a - 1] = []
    grape[a - 1].append(b - 1)
    indegree[b - 1] += 1

queue = deque()
for i in range(n):
    if indegree[i] == 0:
        queue.append(i)
answer = []
while queue:
    temp = queue.popleft()
    answer.append(temp + 1)
    if temp in grape:
        for go in grape[temp]:
            indegree[go] -= 1
            if indegree[go] == 0:
                queue.append(go)
print(*answer)