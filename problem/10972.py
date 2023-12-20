n = int(input())
data = list(map(int, input().split()))

k = -1
for i in range(n - 1):
    if data[i] < data[i + 1]:
        k = i

m = -1
if k == -1:
    print(k)
else:
    for i in range(k, n):
        if data[k] < data[i]:
            m = max(i, m)
    data[m], data[k] = data[k], data[m]
    a = data[:k+1]
    b = data[k+1:]
    b.sort()
    ab = a + b
    print(*ab)
    