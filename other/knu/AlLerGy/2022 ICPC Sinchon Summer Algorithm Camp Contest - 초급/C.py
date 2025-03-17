p, n = map(int,input().split())
data = list(map(int, input().split()))
data.sort()

answer = 0 
h = 200 - p
index = 0
while True:
    if h <= 0 or index >= n:
        break
    else:
        h -= data[index]
        answer += 1
        # print(answer, h)
    index+=1
print(answer)