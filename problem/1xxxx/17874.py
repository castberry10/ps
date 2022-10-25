a, b, c = map(int, input().split())
if b > a / 2:
    b1 = b
else:
    b1 = a - b
if c > a / 2:
    c1 = c
else:
    c1 = a- c
print(c1 * 4 * b1)
