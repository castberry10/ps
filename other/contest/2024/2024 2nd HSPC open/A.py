N, M, X, Y = map(int, input().split())
# dict = {}
me = list(map(int, input().split()))
ls = []
for i in range(N-1):
    # a = list(map(int, input().split()))
    a = list(input().split())
    a[1] = int(a[1])    
    temp = (Y - (X - a[1]))
    if temp < 0:
        temp = 0
    a[1] = a[1] + temp
    ls.append(a)
ls.sort(key=lambda x : x[1])
ls.reverse()

cnt = 0
i = 0
while True:
    if cnt > M:
        print('NO')
        break
    if i >= N:
        print('YES')
        print(ls[-1][1] - me[1])
        break
    if ls[i][0][2:4] == '24' and ls[i][1] > me[1]:
        if cnt == M:
            if me[1] + Y < ls[i][1]:
                print('NO')
                break
            else:
                print('YES')
                print(ls[i][1] - me[1])
                break
        elif cnt < M:
            cnt += 1
    i += 1
        # 미 완성 풀이