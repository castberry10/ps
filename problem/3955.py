def EEA(a, b) :
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
  
    while r1 :
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
    return r0, s0, t0
# a * s0 + b * t1 = r0 
# 여기서 r0는 gcd

N = int(input())
for i in range(N):
    k, c = map(int, input().split())
    if c == 1:
        if k + 1 > 10 ** 9:
            print('IMPOSSIBLE')
            continue
        else:
            print(k + 1)
            continue
    if k == 1:
        if c > 1:
            print(2)
            continue
        else:
            print(1)
            continue
    r, s, t = EEA(k, c)# a * s0 + b * t1 = r0 <- gcd(a, b)
    # print(r, s, t)
    if r > 1:
        print('IMPOSSIBLE')
        continue
    if t > 10 ** 9:
        print('IMPOSSIBLE')
        continue
    if t > 0:
        print(t)
    else:
        print(t + k)    
