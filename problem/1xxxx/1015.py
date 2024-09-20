n = int(input())
data = list(map(int, input().split()))

sortdata = sorted(data)
answer = [0] * n

for i in range(n):
    answer[i] = sortdata.index(data[i])
    sortdata[sortdata.index(data[i])] = -1
    
print(*answer)