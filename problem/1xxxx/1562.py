n = int(input())
dp = [[[0 for k in range(1024)] for j in range(10)] for i in range(n)]

# dp[자리수][마지막][경로]
for i in range(1, 10):
    dp[0][i][1<<i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            for k in range(1024):
                dp[i][j][k | 1<<j] += dp[i-1][j+1][k]
        elif j == 9:
            for k in range(1024):
                dp[i][j][k | 1<<j] += dp[i-1][j-1][k]
        else:
            for k in range(1024):
                dp[i][j][k | 1<<j] += dp[i-1][j-1][k] + dp[i-1][j+1][k]

# print(sum(dp[n-1][1023])%1000000000)
answer = 0

for i in range(10):
    answer += dp[n-1][i][1023]
    
print(answer % 1000000000)
