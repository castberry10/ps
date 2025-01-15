from collections import deque
n = int(input())
graph={}
visit = set()
ptree = {}
visitptree = []
chilecnt = {}
for i in range(n-1):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = []
    graph[a].append(b)
    
def isPtree(n):
    q = deque()
    
    
        