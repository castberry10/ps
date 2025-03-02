import heapq

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
