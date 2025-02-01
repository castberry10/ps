n, k = map(int, input().split()) 
data = [[0 for j in range(n + 1)] for i in range(n + 1)]

for i in range(n + 1):
    data[i][0] = 1
    data[i][1] = i
    data[i][i] = 1

# 5에서 3개 뽑을때 
# 4에서 3개 + 4에서 2개 
# data[5][3] = data[4][3] + data[4][2]

# 3
# 1
# 1 1
# 1 2 1
# 1 3 3 1
for i in range(2, n + 1):
    for j in range(1, i):
        data[i][j] = (data[i-1][j] + data[i-1][j-1]) % 10007
        
print(data[n][k] % 10007)