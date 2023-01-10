n  = int(input())
max1 = 0
for _ in range(n):
    a, d, g = map(int, input().split())
    sco = 0
    if a == d + g:
        sco = a * (d + g)
        sco *= 2
    else:
        sco = a * (d + g)
    if max1 < sco:
        max1 = sco
print(max1)