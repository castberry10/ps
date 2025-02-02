import sys
input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n)]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    if a > b:
        parent[a] = b

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def is_connected(a, b):
    return find(a) == find(b)

for i in range(m):
    a, b = map(int, input().split())
    if is_connected(a, b):
        print(i + 1)
        break
    else:
        union(a, b)
    if i == m -1:
        print(0)