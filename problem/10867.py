n = int(input())
data = list(set(map(int, input().split())))
data.sort()
print(*data)
