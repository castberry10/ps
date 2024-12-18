n, m = map(int, input().split())
parent = [i for i in range(m + 1)]
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        parent[b] = a
    else:
        parent[a] = b

def is_connected(a, b):
    return find(a) == find(b)
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
data = list(map(int, input().split()))
def is_complate():
    parent_set = set(parent)
    return len(parent_set) == 2
for i in range(m):
    for j in range(m):
        if i == j:
            continue
        else:
            if graph[data[j]-1][data[i]-1] == 1 or graph[data[i]-1][data[j]-1] == 1:
                union(i, j)
if is_complate():
    print("YES")
else:
    print("NO")