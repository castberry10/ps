a, b, c = map(int, input().split())
cnt = 0
while True:
    if cnt * c + a >= b:
        print(cnt)
        break
    cnt += 1