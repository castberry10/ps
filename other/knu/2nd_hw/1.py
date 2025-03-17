# 세그먼트 트리 알고리즘
# 조회, 변경 연산이 O(logN)

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2
tree = [0] * treesize # 세그먼트 트리 크기 구하기

data = list(map(int, input().split()))

def build_tree(): # 세그먼트트리 빌드 O(n)
    for i in range(n):
        tree[treesize//2 + i] = data[i]
    for i in range(treesize//2 - 1, 0, -1):
        tree[i] = max(tree[i * 2], tree[i * 2 + 1])
        
def modify(i, v): # 변경 O(logN)
    i += treesize // 2 - 1
    tree[i] = v
    for j in range(i//2, 0, -1):
        tree[j] = max(tree[j * 2], tree[j * 2 + 1])
    

def get_max(s,e): # 구간합 구하기  O(logN)
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

for i in range(q): # q번 순회 O(q log N)
    a, b, c = map(int, input().split())
    if a == 1:
        modify(b, c)
    else:
        print(get_max(b,c))