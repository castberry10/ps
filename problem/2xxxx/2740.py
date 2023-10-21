n, m = map(int, input().split())
A = list()
for i in range(n):
    A.append(list(map(int, input().split())))
m, k = map(int, input().split())
B = list()
for i in range(m):
    B.append(list(map(int, input().split())))

C = [[0] * k for _ in range(n)]

for N in range(n):
    for M in range(m):
        for K in range(k):
            C[N][K] += A[N][M] * B[M][K]
for i in range(n):
    print(*C[i])