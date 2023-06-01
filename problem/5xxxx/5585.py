a = 1000
b = int(input())
ans = 0

a -= b

ans += a // 500
a = a % 500

ans += a // 100
a = a % 100

ans += a // 50
a = a % 50

ans += a // 10
a = a % 10

ans += a // 5
a = a % 5

ans += a // 1
a = a % 1

print(ans)

