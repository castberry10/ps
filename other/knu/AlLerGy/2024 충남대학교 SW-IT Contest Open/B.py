
data = list(map(int, input().split()))
a = sum(data) / 20
index20 = data.index(20)
if index20 == 19:
    b = (data[index20] + data[index20 - 1] + data[0]) / 3
else:
    b = (data[index20] + data[index20 - 1] + data[index20 + 1]) / 3

# print(a, b)
if a > b:
    print("Bob")
elif a < b:
    print("Alice")
else:
    print("Tie")