T = int(input())
for _ in range(T):
    N = int(input())
    datalist = [''] * N
    for i in range(N):
        datalist[i] = input()
    tof = True
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            tempdata = datalist[i] + datalist[j]
            tempdatareverse = tempdata[::-1]
            if tempdata == tempdatareverse:
                print(tempdata)
                tof = False
                break
        if tof == False:
            break
    if tof:
        print(0)