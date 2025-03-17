n, m, k = map(int, input().split())

treesize = 1
while treesize < n:
    treesize *= 2
treesize *= 2

tree = [0] * treesize

data = list(map(int, input().split()))

def build():
    for i in range(len(data)):
        tree[i + treesize//2] = data[i]
    for i in range(treesize // 2 - 1, 0, -1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1] 
    
def update(i, v):
    i = i + treesize // 2 - 1
    tree[i] = v
    while i > 0:
        i //= 2
        tree[i] = tree[i * 2] + tree[i * 2 + 1] 

def return_answer(s, e):
    s += treesize // 2 - 1
    e += treesize // 2 - 1
    value = 0
    while s <= e:
        if s % 2 == 1:
            value += tree[s]
            s += 1            
        if e % 2 == 0:
            value += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return value
build()
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c)
    else:
        print(return_answer(b, c))