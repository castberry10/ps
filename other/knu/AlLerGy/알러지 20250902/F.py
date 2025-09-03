n = int(input())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]


x, y, z, c = a[0], a[0], a[0] 
for i in range(1, n):
    if sum((x, y, z)) <= sum((a[0], a[i], z+a[i])):
        z = z + a[i]
        y = a[i]
        c += 1
        continue
    else:
        break
