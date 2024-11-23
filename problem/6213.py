import sys
input = sys.stdin.readline
n, m = map(int, input().split())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [[1e10, -1e10] for _ in range(treesize)]

def build_tree():
    for i in range(treesize//2 - 1, 0, -1):
        tree[i][0] = min(tree[i * 2][0], tree[i * 2 + 1][0])
        tree[i][1] = max(tree[i * 2][1], tree[i * 2 + 1][1])

def get_min_max(s,e):
    s += treesize // 2
    e += treesize // 2 
    getmin = tree[s][0]
    getmax = tree[s][1]
    while s <= e:
        if s % 2 == 1:
            getmin = min(getmin, tree[s][0])
            getmax = max(getmax, tree[s][1])
            s += 1
        if e % 2 == 0:
            getmin = min(getmin, tree[e][0])
            getmax = max(getmax, tree[e][1])
            e -= 1
        s //= 2
        e //= 2
    return (getmin, getmax)

# 1 <- 0
# 2 3
# 4 5 6 7
for i in range(n):
    temp = int(input())
    tree[treesize//2 + i][0], tree[treesize//2 + i][1] = temp, temp
# print(tree)
build_tree()
for i in range(m):
    a, b = map(int, input().split())
    x, y = get_min_max(a - 1, b - 1)
    print(y - x)