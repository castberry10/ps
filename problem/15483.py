#15483.py 최소편집
a = input()
b = input()
asize = len(a)
bsize = len(b)
dp = [[0 for _ in range(asize + 1)] for _ in range(bsize + 1)]
# dp 가로 a size / 세로 b size
# dp[bsize][asize]
for i in range(asize + 1):
    dp[0][i] = i
for i in range(bsize + 1):
    dp[i][0] = i

for i in range(1, bsize + 1):
    for j in range(1, asize + 1):
        if a[j-1] == b[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1] + 1, dp[i-1][j] + 1, dp[i][j-1] + 1)
                # dp[i - 1][j - 1] + 1,  # 대체
                # dp[i - 1][j] + 1,      # 삽입
                # dp[i][j - 1] + 1       # 삭제

print(dp[bsize][asize])