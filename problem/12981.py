import math

a, b, c = map(int, input().split())
min_ = min(a, b, c)
ans = min_ 
a, b, c = a - min_, b - min_, c - min_

ans += a // 3
a %= 3
ans += b // 3
b %= 3
ans += c //3
c %= 3

chls = list((a,b,c))
chls.sort()

if chls[1] == 0:
    pass 
else:
    if a == 0:
        min_ = min(b, c)
        b, c = b - min_, c - min_
        ans += min_
    elif b == 0:
        min_ = min(a, c)
        a, c = a - min_, c - min_
        ans += min_
    elif c == 0:
        min_ = min(a, b)
        a, b = a - min_, b - min_
        ans += min_

ans += math.ceil(a/3)
ans += math.ceil(b/3)
ans += math.ceil(c/3)

print(ans)
