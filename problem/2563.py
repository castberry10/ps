data = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    # y += 10
    for i in range(x, x+10):
        for j in range(y, y+10):
            data[j][i] = 1
answer = 0 
for i in range(100):
    for j in range(100):
        if data[j][i] == 1:
            answer += 1
print(answer)