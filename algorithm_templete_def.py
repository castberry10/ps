def fastPowMod(a,b,m):    # a^b mod m
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m
    return result

#n이 소수인지 판별하는 숫자, a 그에 대한 테스트 값 
def miller_rabin(n, a):
    r = 0
    d = n-1
    
    if a == n:
        return True #뭔가를 해야할 텐데 
    
    while (d % 2 == 0):
        r += 1
        d = d // 2
    x = fastPowMod(a, d, n) # x = a ^ d % n
    
    if x == 1 or x == n-1:
        return True # 소수임 
    
    for i in range(r-1):
        x = fastPowMod(x, 2, n)
        if x == n-1:
            return True #소수 
    return False # 소수 아님 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)