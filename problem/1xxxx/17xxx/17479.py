import sys

A, B, C = map(int, sys.stdin.readline().split())
Ar = dict()
Br = dict()
Cr = set()

Ac = 0
Am = 0

Bc = 0
Bm = 0

Cc = 0
for i in range(A):
    d1, d2 =  sys.stdin.readline().split()
    Ar[d1] = int(d2)
for i in range(B):
    d1, d2 =  sys.stdin.readline().split()
    Br[d1] = int(d2)
for i in range(C):
    Cr.add(sys.stdin.readline().rstrip())
    
n = int(input())

for _ in range(n):
    d = input()
    if d in Ar:
        Ac += 1
        Am += Ar[d]
        
    elif d in Br:
        Bc += 1
        Bm += Br[d]
        
    elif d in Cr:
        Cc += 1 
        
if Cc > 0 and Am + Bm < 50000:
    print("No")
elif (Bc > 0 or Bm > 0) and Am < 20000:
    print("No")
elif Cc > 1:
    print("No")
else:
    print("Okey")

# print("A: ", A)
# print("B: ", B)
# print("C: ", C)
# print("Ac: ", Ac)
# print("Bc: ", Bc)
# print("Cc: ", Cc)
# print("Ar: ", Ar)
# print("Br: ", Br)
# print("Cr: ", Cr)
# print("Am: ", Am)
# print("Bm: ", Bm)