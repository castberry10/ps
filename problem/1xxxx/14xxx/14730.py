n = int(input())
data = []
answer = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 계수 -> coefficient
# 차수 -> degree
# 3
# 3 3
# 2 2
# 1 1
# data = [[3, 3], [2, 2], [1, 1]]

for i in range(len(data)):
    data[i][0], data[i][1] = data[i][0] * data[i][1], data[i][1] - 1

answerc = 0

for i in range(len(data)):
    if data[i][1] < 0:
        pass
    else:
        answerc += data[i][0]
print(answerc)