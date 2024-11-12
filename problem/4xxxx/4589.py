n = int(input())

# data = []
print("Gnomes:")
for i in range(n):
    data = list(map(int, input().split()))
    data2 = sorted(data)
    data3 = data2[::-1]
    
    # print("data:", data, "data2:", data2, "data3:", data3)
    if data == data2 or data == data3:
        print("Ordered")
    else:
        print("Unordered")