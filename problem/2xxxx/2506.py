N = int(input())
P = list(map(int, input().split()))
for i in range(1, N):
    if P[i - 1] != 0 and P[i] != 0:
        P[i] = P[i - 1] + 1
print(sum(P))