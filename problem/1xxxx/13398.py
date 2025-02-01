n = int(input())
data = list(map(int, input().split()))

dp = [0] * n
rdp = [0] * n 
rdp[0] = dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])
    rdp[i] = max(dp[i-1], rdp[i-1] + data[i])
print(max(max(dp), max(rdp)))