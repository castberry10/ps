# 7 8
# ........
# ........
# ..#####.
# ..#...#.
# ..#.....
# ..#...#.
# ..#####.

n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(input())
yx1 = [-1, -1]  #  // 상 / 좌 
yx2 = [0,   0]  #  //// 하 / 우
# print(data)
# print(n, m)
for i in range(n):
    for j in range(m):
        if data[i][j] == '#':
            # print(data[i][j], '#',data[i][j] == '#')
            if yx1 == [-1, -1]:
                yx1 = [i, j]
            yx2 = [i, j]
a, b, c, d = [yx1[0], yx1[1] + (yx2[1] - yx1[1]) // 2], [yx2[0],yx1[1] + (yx2[1] - yx1[1]) // 2], [yx1[0] + (yx2[0] - yx1[0])//2, yx1[1]],[yx1[0] + (yx2[0] - yx1[0])//2, yx2[1]]  #상, 하, 좌, 우 // y x 
# print(yx1, yx2)
# print(a, b, c, d)
if data[a[0]][a[1]] == '.': #상
    print('UP')
if data[b[0]][b[1]] == '.': #하
    print('DOWN')
if data[c[0]][c[1]] == '.': #좌
    print('LEFT')
if data[d[0]][d[1]] == '.': #우
    print('RIGHT')
# 지금 생각해보면 가운데 좌표 하나만 구하면.. 될꺼를 
