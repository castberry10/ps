a = list(map(int, input().split()))
a.sort()
if a[2] == a[0] + a[1]:
    print(1)
elif a[2] == a[0] * a[1]:
    print(2)
else:
    print(3)