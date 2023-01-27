a, b = map(int, input().split())
c, d = map(int, input().split())

ad = a + d 
bc = b + c 

if ad > bc:
    print(bc)
else:
    print(ad)