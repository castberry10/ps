import sys
from collections import deque

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = {}

answerDFS = []
answerBFS = []

for i in range(m):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
for l in graph:
    graph[l].sort()

def dfs(n):
    answerDFS.append(n)
    if n not in graph:
        return
    for i in graph[n]:
        if i not in answerDFS:
            dfs(i)
    
def bfs():
    global n, m, v
    visit = set()
    queue = deque()
    queue.append(v)
    visit.add(v)
    while queue:
        temp = queue.popleft()
        answerBFS.append(temp)
        if temp not in graph:
            continue 
        for i in graph[temp]:
            if i not in visit: 
                queue.append(i)
                visit.add(i)
    print(*answerBFS)


dfs(v)
print(*answerDFS)
bfs()

