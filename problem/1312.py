# 25 7 5 > 2 3.5714285714285716
import math
a , b, n = map(int, input().split())

# c = float(a / b)
# for i in range(n):
#     c *= 10
    
# c = str(c % 10)
# print(c[0])
#--------------------
c = str(float(a / b))
# print(c)
cnt = 0
ch = False
for i in range(len(c)):
    if c[i] == '.':
        ch = True
    if ch:
        
        if n == cnt:
            print(c[i])
            break
        if i + 1 >= len(c):
            print(0)
        cnt += 1
        
    