import heapq
import sys
input = sys.stdin.readline
def prim(graph, start):
    mst = []  
    visited = set() 
    min_heap = [(0, start, None)] 
    
    total_weight = 0  
    
    while min_heap:
        weight, current, previous = heapq.heappop(min_heap)  
        
        if current in visited:
            continue  
        
        visited.add(current)
        total_weight += weight
        
        if previous is not None:
            mst.append((previous, current, weight))

        for neighbor, edge_weight in graph[current]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))
    
    return mst, total_weight

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    temp = a
    
mst, answer = prim(graph=graph, start=temp)
mst.sort(key=lambda a: -a[2])
long = mst[0][2]
# print(mst)
print(answer-long)
    
    