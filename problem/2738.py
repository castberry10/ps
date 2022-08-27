n , m = map(int, input().split())

aM = [list(map(int,input().split())) for _ in range(n)]
bM = [list(map(int,input().split())) for _ in range(n)]
M = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        M[i][j] = aM[i][j] + bM[i][j]

for i in range(n):
    answer = ''
    for j in range(m):
        answer += str(M[i][j]) + ' '
    print(answer)

