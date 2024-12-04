n = int(input())
data = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = data[0]
for i in range(1, n):
    dp[i] = max(data[i], dp[i - 1]+ data[i])
print(max(dp))