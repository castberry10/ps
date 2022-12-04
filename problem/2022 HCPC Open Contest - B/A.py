N, M = map(int, input().split())
S = list(map(int, input().split()))
T = list()

for _ in range(N):
    T.append(list(map(int, input().split())))

for i in range(N):
    sum_ = 0
    for j in range(len(T)):
        sum_ += T[j][i]
    sum__ = 0 
    for j in range(len(T[i])):
        sum__ += T[i][j]
    print(sum_ + S[i] - sum__, end = ' ')
    # print(sum_ + S[i] - sum(T[j]))

for i in range(M):
    sum_ = 0
    for j in range(len(T)):
        sum_ += T[j][i + N] 
    
    print(sum_, end = ' ')
    
