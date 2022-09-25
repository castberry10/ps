def primeCheck(data):
    if data == 1:
        return False
    for i in range(2, int(data ** 0.5) + 1):
        if data % i == 0:
            return False
    return True



a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

Acnt = 0
Bcnt = 0 

for i in range(a1 , a2 +1 ):
    if primeCheck(i):
        Acnt += 1

for i in range(b1 , b2 +1 ):
    if primeCheck(i):
        Bcnt += 1
# Debug
print(a1, a2, b1, b2)
print(Acnt, Bcnt)

if Acnt > Bcnt:
    print('yt')
else:
    print('yj')