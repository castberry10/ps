import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def solve():
    n = int(input().strip()) 
    parents = list(map(int, input().split())) 

    graph = defaultdict(list)
    for i in range(n-1):
        graph[parents[i]].append(i+2)

    def bfs():
        depth = [-1] * (n + 1)  
        depth[1] = 0 

        queue = deque([1])
        while queue:
            v = queue.popleft()
            for neighbor in graph[v]:
                if depth[neighbor] == -1:
                    depth[neighbor] = depth[v] + 1
                    queue.append(neighbor)
        
        return depth
    depth = bfs()
    depth = depth[2:]
    
    #####
    #정답 코드 넣어야함
    #####
    
    print(depth) 
t = int(input())
for _ in range(t):
    solve()
