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
# 
# 100000000 까지 범위인데 
# 9989899
# 100030001 순 
# <- 
for i in range(1000000000):
    if str(i) == str(i)[::-1] and isPrime(i):
        print(i)