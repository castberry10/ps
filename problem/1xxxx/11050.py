import math # 이항계수: 이항식을 이항 정리로 전개했을 때 각 항의 계수
n, k = map(int, input().split()) 
print(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
