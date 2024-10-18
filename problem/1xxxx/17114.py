#2차원 dfs    / / replit.com
from collections import deque
import sys
input = sys.stdin.readline
# input = iter(open(0).read().split("\n")).__next__

sys.setrecursionlimit(10 ** 9)
NM = list(map(int, input().split()))

box = []
queue = deque()

box = [[[[[[[[[[
    list(map(int, input().split())) for _ in range(NM[1])
] for _ in range(NM[2])
] for _ in range(NM[3])
] for _ in range(NM[4])
] for _ in range(NM[5])
] for _ in range(NM[6])
] for _ in range(NM[7])
] for _ in range(NM[8])
] for _ in range(NM[9])
] for _ in range(NM[10])
]


answer = 0
# dxy = [(0, -1), (0, 1), (1, 0), (-1, 0)]
dxy = [(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
       (-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
       (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
       ]
# 1 찾아서 큐에 넣기
# print(box)
for a in range(NM[10]):
    for b in range(NM[9]):
        for c in range(NM[8]):
            for d in range(NM[7]):
                for e in range(NM[6]):
                    for f in range(NM[5]):
                        for g in range(NM[4]):
                            for h in range(NM[3]):
                                for i in range(NM[2]):
                                    for j in range(NM[1]):
                                        for k in range(NM[0]):
                                            # print(a, b, c, d, e, f, g, h, i, j, k)
                                            if box[a][b][c][d][e][f][g][h][i][j][k] == 1:
                                                queue.append([a,b,c,d,e,f,g,h,i,j,k])

while queue:
    a,b,c,d,e,f,g,h,i,j,k = queue.popleft()

    
    for dxyi in range(22):
        da, db, dc, dd, de, df, dg, dh, di, dj, dk = dxy[dxyi]
        if 0 <= da + a < NM[10] and 0 <= b + db < NM[9] and 0<= c + dc < NM[8] and 0 <= d + dd < NM[7] and 0<= e + de < NM[6] and 0 <= f + df < NM[5] and 0 <= g + dg < NM[4] and 0 <= h + dh < NM[3] and 0 <= i + di < NM[2] and 0<= j + dj < NM[1] and 0<= k + dk < NM[0]:
            if box[a + da][b+db][c+dc][d+dd][e+de][f+df][g+dg][h+dh][i+di][j+dj][k+dk] == 0:
                box[a + da][b+db][c+dc][d+dd][e+de][f+df][g+dg][h+dh][i+di][j+dj][k+dk] += box[a][b][c][d][e][f][g][h][i][j][k] + 1
                queue.append([a+da,b+db,c+dc,d+dd,e+de,f+df,g+dg,h+dh,i+di,j+dj,k+dk])


ck = 1
for a in range(NM[10]):
    if ck == 0:
        break
    for b in range(NM[9]):
        if ck == 0:
            break
        for c in range(NM[8]):
            if ck == 0:
                break
            for d in range(NM[7]):
                if ck == 0:
                    break
                for e in range(NM[6]):
                    if ck == 0:
                        break
                    for f in range(NM[5]):
                        if ck == 0:
                            break
                        for g in range(NM[4]):
                            if ck == 0:
                                break
                            for h in range(NM[3]):
                                if ck == 0:
                                    break
                                for i in range(NM[2]):
                                    if ck == 0:
                                        break
                                    for j in range(NM[1]):
                                        if ck == 0:
                                            break
                                        for k in range(NM[0]):
                                            if ck == 0:
                                                break
                                            if box[a][b][c][d][e][f][g][h][i][j][k] == 0:
                                                ck = 0
                                                break
                                            if box[a][b][c][d][e][f][g][h][i][j][k] > answer:
                                                answer = box[a][b][c][d][e][f][g][h][i][j][k]
# print(box)
if ck == 0:
    print(-1)
else:
    print(answer - 1)
    # 나중에 최적화 필요함