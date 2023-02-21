import sys
n, m = map(int, input().split())
data = []
ps = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
# 1 2    0 0 0
# 3 4    0 1 3
#        0 4 10
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ps[i][j] = data[i-1][j-1] + ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1]
        
#########
# debug #
#########

# print("ps = ")
# for i in range(n + 1):
#     for j in range(n + 1):
#         print(ps[i][j], end = " ")
#     print()



for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    # print(ps[y2][x2], ps[y2][x1], ps[y1][x2], ps[y1][x1])
    print(ps[y2][x2]-ps[y2][x1 - 1]-ps[y1 - 1][x2]+ps[y1 - 1][x1 - 1])
    