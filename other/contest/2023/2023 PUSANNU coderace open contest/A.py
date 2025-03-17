N = int(input())
H = list(map(int, input().split()))
answer = 0 

for i in range(len(H) - 1):
    if H[i] <= H[i + 1]:
        answer += 1
print(answer + 1)