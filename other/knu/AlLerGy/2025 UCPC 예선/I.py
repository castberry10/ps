import sys
input = sys.stdin.readline
import copy  


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


n = int(input())
parent = [i for i in range(n)]
union_size = [1 for _ in range(n)]

data = []

for i in range(n):
    data.append(int(input()))

y_g = 0
x_set = []
x_1_set = []
cnt = 0
x_set.append(data[0])

for i in range(1, n): # 2번 부터
    if data[i-1] >= data[i]: # x 값이 변한것 같으면
        x_1_set = copy.deepcopy(x_set)
        x_set = []
        x_set.append(data[i])
        if data[i] in x_1_set: # 
            union(i - len(x_1_set) + x_1_set.index(data[i]), i)
            print(i - len(x_1_set) + x_1_set.index(data[i]), i)
    else:
        union(i, i-1)
        x_set.append(data[i])
        if data[i] in x_1_set:
            print(i - len(x_1_set) + x_1_set.index(data[i]), i)
            union(i - len(x_1_set) + x_1_set.index(data[i]), i)


parent_set = set(find(i) for i in range(len(parent)))
print(parent)
print(len(parent_set))
print(n)