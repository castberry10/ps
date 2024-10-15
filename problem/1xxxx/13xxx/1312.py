a , b, n = map(int, input().split())
c = a // b
a = a % b 
for i in range(1000003):
    a *= 10
    if n == i + 1:
        print(a // b)
        break
    a = a % b