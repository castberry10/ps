import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def union(a, b):
    A = find(a)
    B = find(b)
    if A != B:
        if A < B:
            parent[B] = A
        else:
            parent[A] = B

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def is_connected(a, b):
    return find(a) == find(b)
answer = 0
for i in range(m):
    a, b = map(int, input().split())
    if is_connected(a, b):
        # print("is_con")
        answer += 1
        continue
    else:
        union(a, b)
for i in range(n):
    find(i + 1)
setg = set(parent)
# print(parent)
# print(setg)
answer += len(setg) - 2
print(answer)