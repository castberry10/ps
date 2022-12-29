n = int(input())

data = list(map(int, input().split()))
cnt = 0

if n == 1:
    if data[0] > 1440:
        print(-1)
    else:
        print(data[0])
else:
    while True:
        data.sort()
        if data[-1] == 0:
            if cnt > 1440:
                print(-1)
                break
            else:
                print(cnt)
                break
        if data[-1] > 0:
            data[-1] -= 1
        if data[-2] >0:
            data[-2] -= 1
        cnt += 1