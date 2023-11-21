def islen3(x):
    return len(x) == 3

n = int(input())
data = []
for i in range(n):
    data.append(input())

data3 = list(filter(islen3, data))

data3.sort()

print(data3[0])
