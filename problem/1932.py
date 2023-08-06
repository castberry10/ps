n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4
#    0     | 0
#   0 0    | 1
#  0 0 0   | 2
# 0 0 0 0  | 3
# print(data)
for i in range(1, n):
    for j in range(i + 1):
        if j == 0: # 왼쪽
            data[i][j] += data[i-1][0]
        elif j == i: # 오른쪽
            data[i][j] += data[i-1][j-1]
        else: # 중간
            data[i][j] += max(data[i-1][j-1], data[i-1][j])
# print(data)
print(max(data[n-1]))