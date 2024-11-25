import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    b, p, q = map(int, input().split())
    treesize = 1
    while treesize < b:
        treesize *= 2
    treesize *= 2

    tree = [0] * treesize

    def plus_num(i, v):
        i += treesize // 2 - 1
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
    
    for i in range(p + q):
        a, b, c = input().split()
        b, c = int(b), int(c)
        if a == "P":
            plus_num(b, c)
        else:
            print(get_sum_num(b, c))