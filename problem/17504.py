n = int(input())
data = list(map(int, input().split()))

datar = data[::-1]
temp = 1
a, b = 1, 1 # a / b 

for i in range(len(datar)):
    if i == 0:
        b = datar[i]
        continue
    a = datar[i] * b + a
    a, b = b, a
print(b - a, b)
    