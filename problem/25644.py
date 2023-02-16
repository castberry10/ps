n = int(input())
data = []

for i in range(n):
    nai, name = list(input().split())
    data.append((nai, i, name))
data.sort(key = lambda x : x[0])
for i in data:
    a, b = i[0], i[2]
    print(a, b)