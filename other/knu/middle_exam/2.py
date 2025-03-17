def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
a, b = map(int, input().split())
answer = -1
for i in range(a, b + 1):
    if isPrime(i):
        answer = i
print(answer)