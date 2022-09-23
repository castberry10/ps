m1, m2 = map(int, input().split())
c = int(input())

if (m1 + m2) >= 2 * c:
    s = (m1 + m2) - 2 * c
    print(s)
else:
    print(m1 + m2)