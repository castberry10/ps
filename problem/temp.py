# # def fastPowMod(a, x, n):    # a^x mod n
# #     y = 1
# #     # 고속 거듭제곱 모듈러 
# #     while x > 0:
# #         if x & 1  == 1: 
# #             y = (a * y) % n     
# #         a = (a * a) % n         
# #         x = x >> 1
        
# #     return y

# def fastPowMod(a,b,m):
#     result = 1
#     while b > 0:
#         if b % 2 != 0:
#             result = (result * a) % m
#         b //= 2
#         a = (a * a) % m

#     return result

# # def fastPowMod(a, x, n):    # a^x mod n
# #     return a ** x % n


# print(fastPowMod(2, 101, 101))

# print(fastPowMod(7, 101, 101))

# print(fastPowMod(61, 101, 101))

# import sys
# n = int(input())
# answer = 0
# # # primelist = [2, 3, 5, 7, 11, 13, 61]
# # primelist = [2, 7, 61]

def fastPowMod(a,b,m):    # a^b mod m
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

def primeCheck(n):
    primeN = True
    
    if n > 2:
        if fastPowMod(2, n, n) == 2:
            pass
        else:
            # print(2, fastPowMod(2, n, n))
            primeN = False
            return primeN
    if n > 3:
        if fastPowMod(3, n, n) == 3:
            pass
        else:
            # print(3, fastPowMod(3, n, n))
            primeN = False
            return primeN
    
    if n > 7:
        if fastPowMod(7, n, n) == 7:
            pass
        else:
            # print(7, fastPowMod(7, n, n))
            primeN = False
            return primeN
    
    if n > 61:
        if fastPowMod(61, n, n) == 61:
            pass
        else:
            # print(61, fastPowMod(61, n, n))
            primeN = False
            return primeN
    
    
    return primeN

# for i in range(n):
#     S = sys.stdin.readline().rstrip()
#     S = int(S)
#     ses = 2 * S + 1 
#     for i in range 
#     # if primeCheck(ses):
#         # print(primeCheck(ses), ses)
#         answer += 1
        


def powmod(a,b,m):
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result

def mr(n,a):
    r = 0
    d = n-1
    while (d%2 != 0):
        print(d, r)
        r += 1
        d = d // 2
    x = powmod(a,d,n)
    if x == 1 or x == n-1:
        return True
    for i in range(0,r-1):
        x = powmod(x,2,n)
        print(3)
        if x == n-1:
            return True
    return False

for i in range(2, 100000):
    print(1)
    a = primeCheck(i)
    b = True
    for i in [2, 3,5,7,11]:
        print(2)
        if mr(b,i) == False:
            b = False
    if a != b:
        print(i, a, b)
# print(answer)
