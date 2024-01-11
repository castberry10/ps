n = int(input())
a = dict()

for i in range(n):
    z, x = input().split()
    x = int(x)
    a[z] = x
jinjucost = a['jinju']
c = 0

for i in a:
    if i == 'jinju':
        pass
    else:
        if jinjucost < a[i]:
            c += 1

print(jinjucost)
print(c)