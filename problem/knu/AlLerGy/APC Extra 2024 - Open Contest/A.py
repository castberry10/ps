n = int(input())
data = set(input().split())
data2 = set(input().split())

for i in data2:
    data.discard(i)
print(*list(data))