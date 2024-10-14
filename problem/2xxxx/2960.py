N, K = map(int, input().split())
datamap = [i for i in range(N + 1)]

datamap[0] = 99999
datamap[1] = 99999
cnt = 0
flag = 0
answer = 0
while True:
    if flag == 1:
        break
    P = min(datamap)
    Pcnt = 1
    while True:
        # print(Pcnt, P)
        # print(datamap)
        if Pcnt * P > N:
            break
        if datamap[Pcnt * P] == 99999:
            Pcnt += 1
        else:
            datamap[Pcnt * P] = 99999
            
            cnt += 1
            if cnt == K:
                answer = Pcnt * P
                flag = 1
            Pcnt += 1
print(answer)