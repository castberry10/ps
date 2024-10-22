def primeCheck(data):
    if data == 1:
        return False
    for i in range(2, int(data ** 0.5) + 1):
        if data % i == 0:
            return False
    return True



a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

Acnt = []
Bcnt = [] 

for i in range(a1 , a2 +1 ):
    if primeCheck(i):
        Acnt.append(i)

for i in range(b1 , b2 +1 ):
    if primeCheck(i):
        Bcnt.append(i)
tof = True 
answerset = set()
answermax = 0

s = set(Acnt) & set(Bcnt)

if len(s) % 2 == 0:
    tof = True 
else:
    tof = False
answerset = s

# print(Acnt, Bcnt)
while True:
    if tof:
        c = True
        for i in Acnt:
            a = len(answerset)
            answerset.add(i)
            b = len(answerset)
            # print(a, b, answerset, i, c, tof)
            if a != b:
                c = False
                break
        if c:
            print('yj')
            break
    else:
        c = True
        for i in Bcnt:
            a = len(answerset)
            answerset.add(i)
            b = len(answerset)
            # print(a, b, answerset, i, c, tof)
            if a != b:
                c = False
                break
        if c:
            print('yt')
            break
    tof = not tof 
# Acnt = set(Acnt)
# Bcnt = set(Bcnt)

# # Debug
# print(a1, a2, b1, b2)
# print(Acnt, Bcnt)

