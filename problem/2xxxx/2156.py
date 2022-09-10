N = int(input())
ls = [0 for _ in range(N + 2)]
dp = [0 for _ in range(N + 2)]

for i in range(N):
    ls[i + 1] = int(input())

dp[1] = ls[1]
dp[2] = ls[1] + ls[2]

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1 ], dp[i - 2] + ls[i], dp[i - 3] + ls[i - 1] + ls[i])

print(dp[N])
# 0 6 10 13 9 8 1 
# 0 0 0  0  0 0 0 