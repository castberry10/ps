n, w, h = map(int, input().split())

max_ = (w ** 2 + h ** 2) ** (1/2)
ans = 0

for i in range(n):
    a = int(input())
    if a <= max_:
        print('DA')
    else:
        print('NE')