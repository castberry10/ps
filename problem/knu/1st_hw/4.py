from collections import deque
import itertools
from functools import reduce

def isPrime(n): # 나름 최적화된 소수 판별 O(n ** 0.5)
    if n == 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a, b): # O(log N) 유클리드호제법
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
ls = list(map(int, input().split()))
primeList = []
for i in range(n): # 순회하며 글자수 합산 + 소수체크
    if isPrime(sum(map(int, list(str(ls[i]))))):
        primeList.append(ls[i])

if len(primeList) < 2:
    print(-1)
else:
    primeList = [gcd(*i) for i in itertools.combinations(primeList, 2)] # 콤비네이션 O(N^2) 
    print(max(primeList))