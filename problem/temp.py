a , b = int(input())
c = 0
a100 = a / 100
b100 = a100 * b
ab = a - b100
if ab < 100:
    print(1)
else:
    print(0)