import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m =map(int, input().split())
parent = [i for i in range(n + 1)]
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
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if is_connected(b, c):
            print("YES")
        else:
            print("NO")
