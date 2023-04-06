cnt = 1
n = int(input())
while True:
    if n == 1:
        print(cnt)
        break
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    cnt += 1