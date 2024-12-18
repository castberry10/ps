# import heapq

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort(key=lambda x : (x[1], x[0]))
answer = 0
time = 0
for i in data:
    starttime, endtime = i[0], i[1]
    if time <= starttime:
        answer += 1
        time = endtime
print(answer)