n, t = map(int, input().split())
wdata = list()
vdata = list()

for i in range(n):
    a, b = map(int,input().split())
    
    wdata.append(a)
    vdata.append(b)
    
def d(n, k, weight, v): # k는 가능무게 n은 item 수 
    dp = [[0] * (k + 1) for _ in range(n+1)] # dp 
    for i in range(1, n + 1):
        for w in range(1, k+1):
            if weight[i-1]<= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - weight[i-1]] + v[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][k]
print(d(n, t, wdata, vdata))