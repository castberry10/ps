import sys
input = sys.stdin.readline
n, q = map(int, input().split())

treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2

tree = [0] * treesize

def modify(i, k):
    i += treesize // 2
    while i > 0:
        tree[i] += k
        i //= 2

def func_sum(s, e):
    s += treesize // 2
    e += treesize // 2
    returnsum = 0
    if s > e:
        s, e = e, s
    while s <= e:
        if s % 2 == 1:
            returnsum += tree[s]
            s += 1
        if e % 2 == 0:
            returnsum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return returnsum

for i in range(q):
    a, b, c = map(int, input().split())
    if a == 1:
        modify(b-1, c)
    if a == 2:
        print(func_sum(b-1, c-1))
    
