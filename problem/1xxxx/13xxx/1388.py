ls = []
n, m = map(int, input().split())
for _ in range(n):
    ls.append(input())

_cnt = 0
lcnt = 0

for i in range(n):
    for j in range(m):
        if ls[i][j] == '-':
            if j == 0 or ls[i-1] != '-':
                _cnt += 1
                
for i in range(m): # 가로 반복
    for j in range(n):
        pass

        #rnlcksgdkek 