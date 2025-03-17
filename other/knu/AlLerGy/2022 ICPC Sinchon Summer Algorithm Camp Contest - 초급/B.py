n = int(input())
a = list(map(int, input().split()))

status = 0
b = 100
somo = 0
for i in range(n):
    if status != a[i]:
        b -= 2
        somo = 2
        status = a[i]
    elif status == a[i]:
        b -= somo * 2
        somo *= 2
    if b <= 0:
        b = 100
        somo = 0
        status = 0
    # print(somo)
    # print(100-b)
print(100-b)