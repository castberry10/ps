import math

n, m = map(int,input().split())

nCm = math.factorial(n)//(math.factorial(m) * math.factorial(n-m))

print(nCm)