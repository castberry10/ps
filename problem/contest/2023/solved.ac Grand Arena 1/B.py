n = int(input())
s = list()
dataset = set()
qindex = 0
for i in range(n):
    data = input()
    s.append(data)
    dataset.add(data)
    if data == '?':
        qindex = i

m = int(input())
a = list()
for i in range(m):
    a.append(input())

if qindex == 0:
    i2 = data[qindex+1]
    i2 = i2[0]
    for i in a:
        if i not in dataset and i[len(i) - 1] == i2:
            print(i)
            break
elif qindex == n - 1:
    i1 = data[qindex-1]
    i1 = i1[len(i1) - 1]
    for i in a:
        if i not in dataset and i1 == i[0]:
            print(i)
            break
else:
    i1 = s[qindex-1]
    i1 = i1[len(i1) - 1]
    i2 = s[qindex+1]
    i2 = i2[0]
    for i in a:
        # print(i)
        # print(i[len(i) - 1], i2, i1, i[0])
        if i not in dataset and i[len(i) - 1] == i2 and i1 == i[0]:
            print(i)
            break
# print(dataset)
# print('s:', s)
# print('a:', a)
