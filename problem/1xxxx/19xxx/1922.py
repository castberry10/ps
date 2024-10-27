import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
graph = []

n = int(input())
m = int(input())


parent = [i for i in range(n + 1)]
answer = 0 
# union-find 
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y

def is_connected(x,y):
    return find(x) == find(y)

for i in range(m):
    graph.append(list(map(int, input().split())))

graph.sort(key = lambda x : x[2])
edge_count = 0
# 0, 1 -> node, 2 -> cost
for item in graph:
    if not is_connected(item[0], item[1]):
        answer += item[2]
        union(item[0], item[1])
        edge_count += 1
        if edge_count == n - 1:
            break
print(answer)
