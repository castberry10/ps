import sys
input = sys.stdin.readline


while True:
    try:
        n, k = map(int, input().split())
        treesize = 1
        while treesize < n:
            treesize *= 2
        treesize *= 2

        data = list(map(int, input().split()))
        tree = [1] * treesize
        def build():
            for i in range(n):
                if data[i] == 0:
                    tree[treesize//2 + i] = 0
                elif data[i] > 0:
                    tree[treesize//2 + i] = 1
                else:
                    tree[treesize//2 + i] = -1
            for i in range(treesize-1, 0, -1):
                tree[i // 2] *= tree[i]

        def modify(i, k):
            i += treesize // 2 - 1
            if k == 0:
                tree[i] = 0
            elif k > 0:
                tree[i] = 1
            else:
                tree[i] = -1
                
            while i > 1:
                i //= 2
                tree[i] = (tree[i*2] * tree[i*2 + 1] )
                

        def func_prod(s, e):
            s += treesize // 2 - 1
            e += treesize // 2 - 1
            returnprod = 1
            while s <= e:
                if s % 2 == 1:
                    returnprod *= tree[s] 
                    s += 1
                if e % 2 == 0:
                    returnprod *= tree[e] 
                    e -= 1
                s //= 2
                e //= 2
            return returnprod
        
        build()
        for i in range(k):
            a, b, c = input().split()
            b, c = int(b), int(c)
            if a == "C":
                modify(b, c)
            if a == "P":
                temp = func_prod(b, c)
                if temp == 0:
                    print("0", end="")
                elif temp < 0:
                    print("-", end="")
                else:
                    print("+", end="")
        print()

    except Exception:
        break
print()