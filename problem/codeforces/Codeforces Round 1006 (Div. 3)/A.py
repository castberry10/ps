def func(n, k, p):
    s = 0
    d = k - s
    if abs(d) > n * p:
        return -1
    r = abs(d) // p
    if abs(d) % p != 0:
        r += 1
    return r

t = int(input())

for _ in range(t):
    n, k, p = map(int, input().split())
    print(func(n, k, p))

