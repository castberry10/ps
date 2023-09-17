y, m, d = map(int, input().split('-'))
a = int(input())

m -= 1
d -= 1

d += a
if d >= 30:
    m += d // 30
    d = d % 30
    # if d == 0:
    #     d = 1
if m >= 12:
    y += m // 12
    m = m % 12
    # if m == 0:
    #     m = 1

m += 1
d += 1
print('{0}-{1:0>2}-{2:0>2}'.format(y,m,d))