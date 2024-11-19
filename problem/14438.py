import sys
input = sys.stdin.readline
n = int(input())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [1e10] * treesize

def build_tree():
    for i in range(treesize//2 - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

def change_value(i, k):
    i += treesize // 2 - 1
    tree[i] = k
    while i > 1:
        i //= 2
        tree[i] = min(tree[i * 2], tree[i*2+1])

def get_min(s,e):
    s += treesize // 2 - 1
    e += treesize // 2 - 1
    getmin = tree[s]
    while s <= e:
        if s % 2 == 1:
            getmin = min(getmin, tree[s])
            s += 1
        if e % 2 == 0:
            getmin = min(getmin, tree[e])
            e -= 1
        s //= 2
        e //= 2
    return getmin


data = list(map(int, input().split()))
for i in range(n):
    tree[treesize//2+i]=data[i]

build_tree()

m = int(input())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        change_value(b, c)
    else:
        print(get_min(b, c))