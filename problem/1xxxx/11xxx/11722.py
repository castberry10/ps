# N = int(input())

# A = list(map(int, input().split()))
# A.insert(0, 1000)
# dp = [1000] * (N + 2)

# mindp = 1000
# for i in range(1, N + 1):  #시작 부분 결정
#     for j in range(i):
#         if A[i] < A[j]:
#             if dp[i] > dp[j] - 1:
#                 dp[i] = dp[j] - 1
#     if dp[i] < mindp:
#         mindp = dp[i]


# print(1000 - mindp)
N = int(input())

A = list(map(int, input().split()))
A.reverse()
A.insert(0, 0)
dp = [0] * (N + 2)

maxdp = 0
for i in range(1, N + 1):  #시작 부분 결정
    for j in range(i):
        if A[i] > A[j]:
            if dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    if dp[i] > maxdp:
        maxdp = dp[i]


print(maxdp)
