import sys
input = sys.stdin.readline
n = int(input())
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
size = [1] * (n + 1)  # 각 집합의 크기
xy = [[0, 0] for _ in range(n + 1)]
dict_r_x = {}
dict_r_y = {}
bu = set()

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
            size[y_root] += size[x_root]
        else:
            parent[y_root] = x_root
            size[x_root] += size[y_root]
            if rank[x_root] == rank[y_root]:
                rank[x_root] +=1

def is_connected(x, y):
    return find(x) == find(y)

for i in range(1, n + 1):
    x, y = map(int, input().split())
    if x not in dict_r_x:
        dict_r_x[x] = []
    if y not in dict_r_y:
        dict_r_y[y] = []
    dict_r_x[x].append(i)
    dict_r_y[y].append(i)
    xy[i][0] = x 
    xy[i][1] = y


for stations in dict_r_x.values():
    first_station = stations[0]
    for station in stations[1:]:
        union(first_station, station)

for stations in dict_r_y.values():
    first_station = stations[0]
    for station in stations[1:]:
        union(first_station, station)

root_sizes = {}
for i in range(1, n+1):
    root = find(i)
    if root not in root_sizes:
        root_sizes[root] = size[root]

roots_by_size = sorted(root_sizes.items(), key=lambda x: -x[1])
most_common = roots_by_size[:2]

if len(most_common) == 1:
    x = xy[most_common[0][0]][0]
    y_candidate = -10**9
    while (x, y_candidate) in bu:
        y_candidate += 1
    print(x, y_candidate)
else:
    x1 = xy[most_common[0][0]][0]
    y2 = xy[most_common[1][0]][1]
    print(x1, y2)
    

