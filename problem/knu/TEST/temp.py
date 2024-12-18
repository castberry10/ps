import heapq
n = 10
graph ={}
graph_m = []
def dijkstar(start):
    q = []
    time_list = [1e9] * n
    heapq.heappush(q, (0, start))
    time_list[start] = 0
    
    while q:
        time, cu_node = heapq.heappop(q)
        if time_list[cu_node] < time:
            continue
        if cu_node in graph:
            for next, next_time in graph[cu_node]:
                next_plus_time = time + next_time
                if next_plus_time < time_list[next]:
                    pass
def be_fo(start):
    time_list = [1e9] * 9
    time_list[start] = 0
    for i in range(n - 1):
        for u in graph:
            for v, w in graph[u]:
                if time_list[u] != 1e9 and time_list[u] + w < time_list[v]:
                    pass
def f_w():
    ## 인접행렬 그래프 
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph_m[i][j] < graph_m[i][k] + graph_m[k][i]:
                    graph_m[i][j] = graph_m[i][k] + graph_m[k][i]