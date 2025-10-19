import sys
input = sys.stdin.readline
n = int(input())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [[1e10, 0] for i in range(treesize)]

def build_tree():
    for i in range(treesize//2 - 1, 0, -1):
        if tree[i * 2][0] == tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2][0]
            tree[i][1] = min(tree[i * 2][1], tree[i * 2 + 1][1])
        elif tree[i * 2][0] < tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2][0]
            tree[i][1] = tree[i * 2][1]
        elif tree[i * 2][0] > tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2 + 1][0]
            tree[i][1] = tree[i * 2 + 1][1]

def change_value(i, k):
    i += treesize // 2 - 1
    tree[i][0] = k
    while i > 1:
        i //= 2
        if tree[i * 2][0] == tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2][0]
            tree[i][1] = min(tree[i * 2][1], tree[i * 2 + 1][1])
        elif tree[i * 2][0] < tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2][0]
            tree[i][1] = tree[i * 2][1]
        elif tree[i * 2][0] > tree[i * 2 + 1][0]:
            tree[i][0] = tree[i * 2 + 1][0]
            tree[i][1] = tree[i * 2 + 1][1]

def get_min(s,e):
    s += treesize // 2 - 1
    e += treesize // 2 - 1
    getmin = tree[s][0]
    getindex = tree[s][1]
    while s <= e:
        if s % 2 == 1:
            if getmin == tree[s][0]:
                getindex = min(getindex, tree[s][1])
            elif getmin > tree[s][0]:
                getmin = tree[s][0]
                getindex = tree[s][1]
            elif getmin < tree[s][0]:
                pass
            s += 1
        if e % 2 == 0:
            if getmin == tree[e][0]:
                getindex = min(getindex, tree[e][1])
            elif getmin > tree[e][0]:
                getmin = tree[e][0]
                getindex = tree[e][1]
            elif getmin < tree[e][0]:
                pass
            e -= 1
        s //= 2
        e //= 2
    return getindex


data = list(map(int, input().split()))
for i in range(n):
    tree[treesize//2+i][0]=data[i]
    tree[treesize//2+i][1]=i + 1

build_tree()

m = int(input())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        change_value(b, c)
    else:
        print(get_min(b, c))