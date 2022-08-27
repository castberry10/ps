# Least Common Multiple: LCM
# Greatest Common Divisor: GCD
# 15 6 > 15 % 6 = 3
# 6 % 3 > 0 ----- > 3 (GCD) 

# 30(LCM) -> 15 * 6 = 90 / GCD => 3 = 30 

def lcm(a, b):
    return a * b / gcd(a, b)
    
# a >= b
def gcd(a, b):
    if a % b: #a를 b로 mod연산시에 결과값(나머지)가 존재하다면
        return gcd(b, a%b)
    else:
        return b
    	
N = int(input())

for _ in range(N):
    a, b  = map(int, input().split())
    print(int(lcm(a, b)))
