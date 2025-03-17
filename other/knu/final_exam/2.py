import heapq

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
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

def is_complate():
    parent_set = set(parent)
    return len(parent_set) == 2

hq = []    
for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(hq, (c, (a, b)))
answer = 0
while hq:
    cost, t = heapq.heappop(hq)
    a, b = t
    # print('a', a)
    # print('b', b)
    if is_connected(a, b):
        continue
    else:
        union(a, b)
        answer += cost
print(answer)            