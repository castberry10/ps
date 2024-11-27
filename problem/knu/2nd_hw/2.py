import sys 
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, input().split())
answer = 0
hq = []

for i in range(m):
    u, v, c = map(int, input().split())
    heapq.heappush(hq, (c, u, v))

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

while hq:
    c, u, v = heapq.heappop(hq)
    if not is_connected(u, v):
        union(u, v)
        answer += c

a, b, c = map(int, input().split())
def solve():
    for i in range(1, n):
        if not is_connected(i, i+1):
            print(-1)
            return
    print(answer)
solve()