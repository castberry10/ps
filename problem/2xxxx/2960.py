N, K = map(int, input().split())
data = list(range(2, N + 1))
temp = 2
cnt = 0
# answer = 0
while True:
    if cnt > K:
        print(answer)
        break
    else:
        
        temp = data[0]
        tempadd = data[0]
        data.remove(temp)
        answer = temp
        cnt += 1
        while True:
            if cnt > K:
                break
            else:
                temp += tempadd
                data.remove(temp)
                answer += temp
                cnt += 1
print(answer)