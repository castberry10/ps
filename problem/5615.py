import sys
n = int(input())
answer = 0
# # primelist = [2, 3, 5, 7, 11, 13, 61]
# primelist = [2, 7, 61]

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
        
for i in range(2, 100000):
    if primeCheck(i):
        print(i)
        answer += 1
print(answer)