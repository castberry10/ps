from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = {}
fnlist = 0
for i in range(n-1):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)
    
def bfs(n):
    global fnlist
    q = deque()
    visit = set()
    visit.add(0)
    visit.add(n)
    q.append(0)
    while q:
        currentNode = q.popleft()
        if currentNode in graph:
            for nextNode in graph[currentNode]:
                if nextNode not in visit:
                    visit.add(nextNode)
                    q.append(nextNode)
    visit.remove(n)
    visit.remove(0)
    temp = 0
    for i in visit:
        temp += 2 ** (i-1)
    fnlist ^= temp

for i in range(n-1):
    bfs(i+1)
    
binary = bin(fnlist)[2:]
if len(binary) < n-1: # 2 < 4 
    binary = ('0' * ((n - 1) - len(binary))) +binary
print(binary)