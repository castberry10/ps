n = int(input())
data = list(map(int, input().split()))
data.sort()

data1 = []
data2 = []

i = 0
while True:
    if i == len(data):
        break
    data1.append(data[i])
    i += 1
    if i == len(data):
        break
    data2.append(data[i])
    i += 1

answer = 0

if len(data1) == 1:
    answer += 1
elif len(data1) > 1:
    answer += 1
    for i in range(1, len(data1)):
        if data1[i - 1] < data1[i]:
            answer += 1

if len(data2) == 1:
    answer += 1
elif len(data2) > 1:
    answer += 1
    for i in range(1, len(data2)):
        if data2[i - 1] < data2[i]:
            answer += 1



if (len(data1) > 1 and data1[-1] == data1[-2] and data1[-1] > data2[-1]) or (len(data2) > 1 and data2[-1] == data2[-2] and data2[-1] > data1[-1]):
    answer += 1

print(answer)