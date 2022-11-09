a, b, c = map(int, input().split())

if a * a + b * b == c * c or c * c + b * b == a * a or a * a + c * c == b * b:
    print(1)
elif a == b == c:
    print(2)
else:
    print(0)