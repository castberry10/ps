n = int(input())
data = list(map(int, input().split()))

data.sort()
# sumdata = [0] * n
for i in range(1, n):
    data[i] = data[i - 1] + data[i]
print(sum(data))