a = int(input())
b = int(input())
d1, d2, d3 = map(int, input().split())

a -= b

INF = 10**6
dp = [INF] * (a + 1)
dp[0] = 0  

for unit in [d1, d2, d3]:
    for i in range(unit, a + 1):
        dp[i] = min(dp[i], dp[i - unit] + 1)

if dp[a] == INF:
    print(-1)
else:
    print(dp[a])
