data = [0] * 10
for i in range(5):
    n = int(input())
    data[n] += 1
# print(data)
for i in range(10):
    if data[i] % 2 == 1:
        print(i)
        break    