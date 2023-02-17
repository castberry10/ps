a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a * 1000)
elif a == c:
    print(a *  100 + 1000)
elif b == c:
    print(b *  100 + 1000)
elif a == b:
    print(a * 100 + 1000)
else:
    print(max((a, b, c)) * 100)