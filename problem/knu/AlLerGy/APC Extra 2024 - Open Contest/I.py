x, y, z = map(int ,input().split())
temp = min(x, y, z)
if temp <= 2:
    print(0)
elif x == y == z == 3:
    print(0) 
else:
    print((temp - 1) // 2)
