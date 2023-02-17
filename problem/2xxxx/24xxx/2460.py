max1 = 0
temp = 0
for _ in range(10):
    a, b = map(int, input().split())
    temp += b - a 
    if temp > max1:
        max1 = temp
print(max1)
    