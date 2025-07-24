from collections import Counter

n, m, k = map(int, input().split())
data = list()
# data = array = [[{"value": 0} for _ in range(k)] for _ in range(k)]
# data2 = ["A" * k for _ in range(k)]
for i in range(n):
    data.append(input())
data = list(map(list, data))
answer = 0
for t in range(k * k):
    cnt = []
    for i in range(n // k):
        for j in range(m // k):
            x = t % k
            y = t // k          
            cnt.append(data[k * i + y][k * j + x])
    counter = Counter(cnt)
    # print(counter)
    temp = counter.most_common(1)[0]
    for i in range(n // k):
        for j in range(m // k):
            x = t % k
            y = t // k   
            if data[k * i + y][k * j + x] != temp[0]:
                answer += 1
                data[k * i + y][k * j + x] = temp[0]
print(answer)
for i in range(n):
    print(str.join('', data[i]))