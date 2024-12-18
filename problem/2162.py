import sys
input = sys.stdin.readline

n = int(input())

parent = [i for i in range(n)]
union_size = [1 for _ in range(n)]

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

def is_connected(a, b):
    return find(a) == find(b)

def ccw(x1, y1, x2, y2, x3, y3):
    return ((x2-x1)*(y3-y2)) - ((x3-x2)*(y2-y1))

def isOverlap(x1, y1, x2, y2, x3, y3, x4, y4):
    # P1 - x1, y1, x2, y2 
    # P2 - x3, y3, x4, y4
    return min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2) 


def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    #x1, y1, x2, y2, x3, y3, x4, y4
    #를 점 a b c d 라 한다면
    abc = ccw(x1, y1, x2, y2, x3, y3)
    abd = ccw(x1, y1, x2, y2, x4, y4)
    cda = ccw(x3, y3, x4, y4, x1, y1)
    cdb = ccw(x3, y3, x4, y4, x2, y2)

    if abc * abd == 0 and cda * cdb == 0:
        return isOverlap(x1, y1, x2, y2, x3, y3, x4, y4)
    return abc * abd <= 0 and cda * cdb <= 0

data = []
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(len(data)):
        if isCross(x1, y1, x2, y2, data[j][0], data[j][1], data[j][2], data[j][3]):
            union(i, j)
    data.append(list((x1, y1, x2, y2)))
for i in range(n):
    find(i)

parent_set = set(parent)

print(len(parent_set))
print(max(union_size))
# print("parent", parent)