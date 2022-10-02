N = int(input())
# A = []
A = list(map(int, input().split()))

dp = [0] * N 
maxdata = 0
maxdp = 0
for i in range(N):
    if A[i] > maxdata:
        if i == 0:
            maxdata = A[0]
            dp[0] = 1
            continue
        # print()
        maxdata = A[i]
        maxdp = max(dp[:i])
        dp[i] = maxdp + 1
        
# print(dp)
# print(A)
print(max(dp))