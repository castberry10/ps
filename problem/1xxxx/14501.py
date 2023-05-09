N = int(input()) # 상담 가능 기간
data = [list(map(int, input().split())) for i in range(N)]
# data > [[3, 10], [5, 20], . . . ]
# data[x][0] -> 상담에 걸리는 시간, data[x][1] -> 상담 비용
dp = [0] * (N + 2)
# Top - down / dynamic programming
for i in range(N - 1, -1, -1):
    if i + data[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i+1], data[i][1] + dp[i + data[i][0]])

        
print(dp[0])