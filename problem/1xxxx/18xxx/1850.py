a, b = map(int, input().split())
# tempa, tempb = a, b
if b > a:
    a, b = b, a
while True:
    if a % b == 0:
        break
    else:
        a, b = b, a % b
print('1' * b)