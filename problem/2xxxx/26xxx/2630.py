n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
whitepaper = 0
bluepaper = 0

# 0 1 2 3 <- m

# 1 1 0 0  0 <- n
# 1 1 0 0  1
# 0 0 0 0  2
# 0 0 0 1  3

# 0 0 4
# > 0 0 2 / 0 2 2 / 2 0 2 / 2 2 2
#
# 2 2 2 
# > 3 3 1 / 3 4 1 / 4 3 1 / 4 4 1
def cntF(x, y, c): #초기는 0 0 4 이라 하면
    global whitepaper
    global bluepaper
    # print(x, y, c)
    ck = True
    for i in range(y, y + c):
        for j in range(x, x + c):
            if paper[x][y] != paper[j][i]:
                
                
                ck = False
                c2 = c // 2
                cntF(x, y, c2)
                cntF(x + c2, y, c2)
                cntF(x, y + c2, c2)
                cntF(x + c2, y + c2, c2)
                return
        if not ck:
            break
    if ck:
        color = paper[x][y] #사실 y x긴 한데 
        if color == 0:
            whitepaper += 1
        else:
            bluepaper += 1
    return
cntF(0, 0, n)

print(whitepaper)
print(bluepaper)