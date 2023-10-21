n, m = map(int, input().split())

data = [[m+1 for _ in range(100)] for _ in range(100)]
answer = 0
# print(data)
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            data[j][i] -= 1

for i in range(100):
    for j in range(100):
        if data[j][i] <= 0:
            answer += 1
print(answer)

