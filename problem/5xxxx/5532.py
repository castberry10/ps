import math

l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

a1 = math.ceil(a / c)
a2 = math.ceil(b / d)

temp = max(a1, a2)

print(l - temp)