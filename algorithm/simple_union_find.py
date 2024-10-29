e = 10
parent_node = [i for i in range(e + 1)]

# union-find 
def find(x):
    if x == parent_node[x]:
        return x
    parent_node[x] = find(parent_node[x])
    return parent_node[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x < y:
        parent_node[y] = x
    else:
        parent_node[x] = y

def is_connected(x,y):
    return find(x) == find(y)

rank = [0] * (e + 1)  # 랭크
size = [1] * (e + 1)  # size

def union_by_rank(x, y):
    # 두 집합을 랭크 기반으로 합치는 함수
    # 랭크가 더 낮은 트리를 높은 트리 아래에 붙여 트리의 높이를 최소화
    x = find(x)
    y = find(y)
    
    if x != y:
        if rank[x] > rank[y]:
            parent_node[y] = x
        elif rank[x] < rank[y]:
            parent_node[x] = y
        else:
            parent_node[y] = x
            rank[x] += 1


def union_by_size(x, y):
    # 두 집합을 크기 기반으로 합치는 함수
    # 더 작은 집합을 더 큰 집합 아래에 붙여 트리의 크기를 최소화
    x = find(x)
    y = find(y)
    
    if x != y:
        if size[x] > size[y]:
            parent_node[y] = x
            size[x] += size[y]
        else:
            parent_node[x] = y
            size[y] += size[x]
