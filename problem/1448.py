import sys

input = sys.stdin.readline 
n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

data.sort()
data.reverse()
for i in range(n - 2):
    if data[i] < data[i + 1] + data[i + 2]:
        print(data[i] + data[i + 1] + data[i + 2])
        break
    else:
        if i == n - 3:
            print(-1)
        