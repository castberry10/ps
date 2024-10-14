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
def miller_rabin_check():
    pass 
# import sys
# n = int(input())
# answer = 0

# for i in range(n):
#     S = sys.stdin.readline().rstrip()
#     S = int(S)
#     ses = 2 * S + 1 
#     checklist = [2, 3, 5, 7, 11]
#     flag = True
#     for i in checklist:
#         if not miller_rabin(ses, i):
#             flag = False
#             break
#     if flag:
#         answer += 1
# print(answer)


# #오일러 피 함수 구현
# import math
# N = int(input())
# answer = N

# for p in range(2, int(math.sqrt(N)) + 1):
#     if N % p == 0:
#         answer = answer - (answer / p)
#         while N % p == 0: #현재의 소인수로 계속나눠서 현재의 소인수가 없게? 하기
#             N /= p

# if N > 1: # N이 1보다 크면 N은 처음 데이터의 남아있는 소인수
#     answer = answer - (answer / N)

# print(int(answer)) # 실수를 내림해 정수로 변환