n, l = map(int,input().split())

data = list(map(int,input().split()))

data.sort()

for i in data:
    if i <= l:
        l += 1
    else:
        break
print(l)