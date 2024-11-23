import sys
input = sys.stdin.readline

n, m = map(int, input().split())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [0] * treesize

data = list(map(int, input().split()))
def build_tree():
    for i in range(n):
        tree[treesize//2 + i] = data[i]
    for i in range(treesize//2 - 1, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])

def get_max(s,e):
    s += treesize // 2 - 1
    e += treesize // 2 - 1
    getmax = tree[s]
    while s <= e:
        if s % 2 == 1:
            getmax = max(getmax, tree[s])
            s += 1
        if e % 2 == 0:
            getmax = max(getmax, tree[e])
            e -= 1
        s //= 2
        e //= 2
    return getmax
build_tree()
answer = []
d = m - 1
for i in range(m, n-m+2):
    answer.append(get_max(i - d, i + d))
print(*answer)