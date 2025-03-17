N, M = map(int, input().split())
data = []

# 덧칠 고려 안함
for _ in range(N):
    data.append(list(map(int, input().split())))

answer = 0

for i in range(N):
    temp = 0
    for j in range(M):
        # if temp == 0 and (data[i][j] == 1 or data[i][j] == 2):
        #     answer += 1
        if data[i][j] == 0:
            pass
        elif temp == 1 and data[i][j] == 1:
            pass
        elif temp == 2 and data[i][j] == 2:
            pass
        else:
            answer +=1
        temp = data[i][j]
        
print(answer)