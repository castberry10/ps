import sys 
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# 유니온 파인드
# 랭크 최적화를 하지않고 경로 압축만 구현했으므로 
# 연산 시간복잡도 O(logN)
n, m, k = map(int, input().split())
answer = 0
hq = []

for i in range(m): # 힙 정렬 O(m log m)
    u, v, c = map(int, input().split())
    heapq.heappush(hq, (c, u, v))

parent = [i for i in range(n + 1)]

def union(a, b): # 합 연산 
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    if a > b:
        parent[a] = b

def find(a): # 부모 찾기 & 경로 압축
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def is_connected(a, b): # 비교연산
    return find(a) == find(b)

# O(m log n)
while hq:
    c, u, v = heapq.heappop(hq) 
    if not is_connected(u, v):
        union(u, v) 
        answer += c

a, b, c = map(int, input().split())
def solve():
    for i in range(1, n): # O(n)
        if not is_connected(i, i+1):
            print(-1)
            return
    print(answer)
solve()