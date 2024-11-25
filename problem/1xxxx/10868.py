import sys
input = sys.stdin.readline
n, m = map(int, input().split())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [1e10] * treesize

def build_tree():
    for i in range(treesize//2 - 1, 0, -1):
        tree[i] = min(tree[i * 2], tree[i * 2 + 1])

def get_min(s,e):
    s += treesize // 2
    e += treesize // 2 
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

# 1 <- 0
# 2 3
# 4 5 6 7
for i in range(n):
    tree[treesize//2 + i] = int(input())
build_tree()
for i in range(m):
    a, b = map(int, input().split())
    print(get_min(a - 1, b - 1))