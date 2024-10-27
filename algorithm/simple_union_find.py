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
# def union(x, y): # 랭크기반 합치기 
#     x = find(x)
#     y = find(y)
#     if x != y:
#         if rank[x] < rank[y]:
#             parent_node[x] = y
#         elif rank[x] > rank[y]:
#             parent_node[y] = x
#         else:
#             parent_node[y] = x
#             rank[x] += 1
def is_connected(x,y):
    return find(x) == find(y)
