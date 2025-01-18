from collections import deque
import sys

input = sys.stdin.readline
n = int(input().strip())

graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dist = [-1] * n

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

bfs(0)
answer_bits = []
for v in range(1, n):
    bit = ((n-1) - dist[v]) % 2
    answer_bits.append(str(bit))

answer_bits.reverse()

print("".join(answer_bits))
