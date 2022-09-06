n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

def cntF():
    ck = 1
    for i in range(n):
        for j in range(n):
            if paper[0][0] != paper[i][j]:
                ck = 0