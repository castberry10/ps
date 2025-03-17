N, A, B = map(int, input().split())
a, b = 1, 1
for i in range(N):
    a += A
    b += B
    if a < b:
        a,b = b,a
    if a == b:
        b -= 1
print(a, b)