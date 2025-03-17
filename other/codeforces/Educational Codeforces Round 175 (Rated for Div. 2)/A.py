def f(n):
    if n < 3:
        return n + 1
    return (n // 15) * 3 + min(3, (n % 15) + 1)


t = int(input()) 
for _ in range(t):
    n = int(input())
    print(f(n))
