# 9251.py LCS2
a = input().rstrip()
b = input().rstrip()

dp = [[0 for i in range(len(a) + 1 )] for j in range(len(b) + 1)]

# 가로가 a 
# 세로가 b 
# 그럼 dp[b][a] dp[i][j]
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j-1] == b[i - 1]:
            dp[i][j] += dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(b)][len(a)])
# answer = ""

def getWalk(a, b):
    asize = len(a)
    bsize = len(b)
    answer = ""
    while dp[bsize][asize] != 0:
        if a[asize - 1] == b[bsize - 1]:
            answer += a[asize - 1]
            asize -= 1
            bsize -= 1
        else:
            if dp[bsize-1][asize] > dp[bsize][asize-1]:
                bsize -= 1
            else:
                asize -= 1
    return answer[::-1]
    

if dp[len(b)][len(a)] != 0:
    print(getWalk(a, b))