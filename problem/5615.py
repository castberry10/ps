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

def miller_rabin(n, a):
    r = 0
    d = n-1
    while (d % 2 == 0):
        r += 1
        d = d // 2
    x = fastPowMod(a, d, n)
    if x == 1 or x == n-1:
        return True
    for i in range(0,r-1):
        x = fastPowMod(x, 2, n)
        if x == n-1:
            return True
    return False


for i in range(n):
    S = sys.stdin.readline().rstrip()
    S = int(S)
    ses = 2 * S + 1 
    # checklist = [2, 7, 61] # 42억아래 결정적 뭐시기 <- ? 
    checklist = [2, 3, 5, 7, 11, 61]
    flag = True
    for i in checklist:
        if not miller_rabin(ses, i):
            flag = False
            break
    if flag:
        answer += 1
print(answer)