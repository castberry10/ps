import sys
input = sys.stdin.readline

n, q = map(int ,input().split())
data = list(map(int, input().split()))
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2

tree = [0] * treesize
def build_tree():
    for i in range(n):
        tree[treesize//2 + i] = data[i]
    for i in range(treesize - 1 , 1 , -1):
        tree[i // 2] += tree[i]
def change_num(i, v):
    i += treesize // 2 - 1
    v = v - tree[i]
    while i:
        tree[i] += v
        i //= 2

def get_sum_num(s, e):
    if e < s:
        s, e = e, s
    sum_num = 0
    s += treesize // 2 - 1
    e += treesize // 2 - 1
    while s <= e:
        if s % 2 == 1:
            sum_num += tree[s]
            s += 1
        if e % 2 == 0:
            sum_num += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return sum_num

build_tree()

for i in range(q):
    a, b, c, d = map(int, input().split())
    print(get_sum_num(a, b))
    change_num(c, d)