n = int(input())
data = list(map(int, input().split()))
dic = dict()
data2 = list(set(data))
data2.sort()
for i in range(len(data2)):
    dic[data2[i]] = i
for i in data:
    print(dic[i], end = " ")