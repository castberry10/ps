
n = int(input())
data = []
for i in range(n):
    ls1, ls2 = map(int, input().split())
    data.append([ls1, ls2])
# print(data)
data.sort(key = lambda x :(x[1], x[0]))

time = 0
endtime = 0
answer = 0
for d in data:
    if time <= d[0]:
        time = d[1]
        answer += 1
        
print(answer)