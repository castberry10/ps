n, m = map(int , input().split())
datamap = {}
for i in range(n):
    k = int(input())
    data = list(map(int, input().split()))
    for j in data:
        if j not in datamap:
            datamap[j] = 1
        else:
            datamap[j] += 1
answer = 0 
for j in datamap:
    if datamap[j] >= m:
        answer += 1
print(answer)