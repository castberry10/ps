data = list(map(int, input().split()))
d = data[0]
a = 0
for i in data:
    if d - 1000 <= i:
        a += 1
print(a - 1)