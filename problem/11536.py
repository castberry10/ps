n = int(input())
data = []

for i in range(n):
    data.append(input())

datas = sorted(data)
datasr = datas[::-1]

if data == datas:
    print('INCREASING')
elif data == datasr:
    print('DECREASING')
else:
    print('NEITHER')