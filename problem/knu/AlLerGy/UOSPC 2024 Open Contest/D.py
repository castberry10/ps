n, k = map(int, input().split())
wkddoanf = set()
for i in range(n):
    x,y = map(int, input().split())
    wkddoanf.add((x, y))
data = input()
x, y = 0, 0 
for i in data:
    if i == 'L':
        x -= 1
        if (x, y) in wkddoanf:
            x += 1
    if i == 'R':
        x += 1
        if (x, y) in wkddoanf:
            x -= 1
    if i == 'U':
        y += 1
        if (x, y) in wkddoanf:
            y -= 1
    if i == 'D':
        y -= 1
        if (x, y) in wkddoanf:
            y += 1
print(*[x, y])