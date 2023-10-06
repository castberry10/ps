n = int(input())

data = [[1 for _ in range(100)] for _ in range(100)]
print(data)
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            data[j][i] = 0
pritn(sum(data))