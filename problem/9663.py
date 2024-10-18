n = int(input())
data = [-1] * (n)
answer = 0

def queen(x): # true면 가능, false 불가능 (두는게)
    global n
    # tof = True
    for i in range(x): # 0 ~ n x 
        if data[i] == data[x] or abs(data[x] - data[i]) == abs(x - i):
            return False
    return True

def bt(cnt):
    global n
    global answer
    # print(data)
    if cnt >= n:
        answer += 1
        return
    for i in range(n):
        data[cnt] = i
        if queen(cnt):
            bt(cnt + 1)
                

bt(0)
print(answer)