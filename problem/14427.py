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

def get_min():
    return tree[1][1]


data = list(map(int, input().split()))
for i in range(n):
    tree[treesize//2+i][0]=data[i]
    tree[treesize//2+i][1]=i + 1

build_tree()

m = int(input())
for i in range(m):
    t = input().strip()
    if t[0] == '1':
        a, b, c = map(int, t.split())
        change_value(b, c)
    else:
        print(get_min())
