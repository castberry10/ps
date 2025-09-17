n, t = map(int, input().split())
data = list(map(int, input().split()))

answer = 0 
for i in range(n):
    if t % data[i] == 0:
        continue
    else:
        temp = []
        for c in range(1, t+1):
            if t % c == 0:
                temp.append(c)
                
        closest = temp[0]
        min_diff = abs(temp[0] - data[i])

        for num in temp:
            diff = abs(num - data[i])
            if diff < min_diff:
                min_diff = diff
                closest = num
        answer += min_diff
print(answer)