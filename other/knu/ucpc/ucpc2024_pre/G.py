import sys
input = sys.stdin.readline

r, c = map(int, input().split())

parent = [i for i in range(r * c * 8)]
union_size = [1 for _ in range(r * c * 8)]

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

for i in range(r):
    data = input()
    for j in range(c):
        temp = 8 * i * c + 8 * j 
        if data[j] == 'I':
            union(temp + 0, temp + 2)
            union(temp + 1, temp + 3)
            union(temp + 4, temp + 6)
            union(temp + 5, temp + 7)
        if data[j] == 'H':
            union(temp + 0, temp + 1)
            union(temp + 2, temp + 3)
            union(temp + 4, temp + 5)
            union(temp + 6, temp + 7)
        if data[j] == 'O':
            union(temp + 0, temp + 4)
            union(temp + 1, temp + 5)
            union(temp + 2, temp + 6)
            union(temp + 3, temp + 7)

for i in range(r - 1): # 세로끼리 연결
    for j in range(c):
        temp = 8 * i * c + 8 * j
        union(temp + 2, temp + 8 * c + 0)
        union(temp + 3, temp + 8 * c + 1)
        union(temp + 6, temp + 8 * c + 4)
        union(temp + 7, temp + 8 * c + 5)
        
for i in range(r): 
    for j in range(c - 1): 
        temp = 8 * i * c + 8 * j
        union(temp + 1, temp + 8 + 0)
        union(temp + 3, temp + 8 + 2)
        union(temp + 5, temp + 8 + 4)
        union(temp + 7, temp + 8 + 6)

parent_set = set(find(i) for i in range(len(parent)))
print(len(parent_set))

