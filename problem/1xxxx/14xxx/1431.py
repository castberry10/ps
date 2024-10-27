n = int(input())
data = []
datasum = dict()
for i in range(n):
    a = input()
    temp = 0
    data.append(a)
    for c in a:
        if c in "123456789":
            temp += int(c)
    datasum[a] = temp

data.sort(key = lambda x : (len(x), datasum[x], x))
for i in data:
    print(i)