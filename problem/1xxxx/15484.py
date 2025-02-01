a = input().strip()
b = input().strip()
asize = len(a)
bsize = len(b)

dp = [[0]*(bsize+1) for _ in range(asize+1)]

for i in range(asize+1):
    dp[i][0] = i
for i in range(bsize+1):
    dp[0][i] = i

da = {}

for i in range(1, asize+1):
    db = 0
    for j in range(1, bsize+1):
        k = da.get(b[j-1], 0)
        l = db

        if a[i-1] == b[j-1]:
            cost = 0
            db = j
        else:
            cost = 1

        dp[i][j] = min(dp[i-1][j-1] + cost,  # substitution
                       dp[i][j-1] + 1,       # insertion
                       dp[i-1][j] + 1)       # deletion


        if k > 0 and l > 0:
            dp[i][j] = min(dp[i][j], dp[k-1][l-1] + (i - k - 1) + 1 + (j - l - 1))

    da[a[i-1]] = i

print(dp[asize][bsize])
