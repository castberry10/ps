n = int(input())
data = []

for i in range(n):
    data.append(input())
data = set(data)
data = list(data)
data.sort(key = lambda x : (len(x), x))

for i in data:
    print(i)