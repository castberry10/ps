import sys
from collections import defaultdict
input = sys.stdin.readline

def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    
    if union_size[a] < union_size[b]:
        parent[a] = b
        union_size[b] += union_size[a]
    else:
        parent[b] = a
        union_size[a] += union_size[b]

n, m, k = map(int, input().split())
stars = set()
for _ in range(k):
    x, y = map(int, input().split())
    stars.add((x - 1, y - 1))   

starts = [tuple(map(int, input().split())) for _ in range(4)]
a1, b1 = starts[0][0] - 1, starts[0][1] - 1
a2, b2 = starts[1][0] - 1, starts[1][1] - 1
a3, b3 = starts[2][0] - 1, starts[2][1] - 1
a4, b4 = starts[3][0] - 1, starts[3][1] - 1

parent = [i for i in range(n * m)]
union_size = [1] * (n * m)

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            continue
        idx = i * m + j
        if i + 1 < n and (i + 1, j) not in stars:
            union(idx, (i + 1) * m + j)
        if j + 1 < m and (i, j + 1) not in stars:
            union(idx, i * m + (j + 1))

cnt1 = defaultdict(int)
cnt2 = defaultdict(int)

for i in range(n):
    for j in range(m):
        if (i, j) in stars:
            continue
        root = find(i * m + j)
        if a1 <= i <= a2 and b1 <= j <= b2:  
            cnt1[root] += 1
        if a3 <= i <= a4 and b3 <= j <= b4:  
            cnt2[root] += 1

answer = 0
for r in set(cnt1) | set(cnt2):
    answer += cnt1[r] * cnt2[r]

print(answer)
