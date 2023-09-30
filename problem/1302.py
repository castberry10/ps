n = int(input())

data = dict()

for i in range(n):
    inputdata = input()
    if inputdata in data:
        data[inputdata] += 1
    else:
        data[inputdata] = 1
sortdata = sorted(data.items(), key = lambda x : (-x[1], x[0]))

print(sortdata[0][0])