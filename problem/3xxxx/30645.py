R, C = map(int, input().split())
N = int(input())
H = list(map(int, input().split()))
# 4 3 
# 0 0 0
# 0 0 0
# 0 0 0
# 0 0 0

data = [[-1 for _ in range(C)] for _ in range(R)]

H.sort()

index = 0
for i in range(R):
    if index >= N:
        break
    for j in range(C):
        if index >= N:
            break
            
        if (i >= 0 and index < N):
            while index < N and data[i-1][j] == H[index]:
                index += 1
        if index >= N:
            break
        data[i][j] = H[index]
        index += 1
answer = 0


for i in range(C):
    for j in range(R):
        if data[j][i] == -1:
            continue
        if j == 0:
            answer += 1
            continue
        if j > 0:
            if data[j][i] > data[j - 1][i]:
                answer += 1
print(answer)