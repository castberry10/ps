def ccw(x1, y1, x2, y2, x3, y3):
    return ((x2-x1) * (y3-y2)) - ((y2-y1) * (x3 - x2))

def isOverlap(x1, y1, x2, y2, x3, y3, x4, y4): 
    if (min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2)):
        return True

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
# L1의 두개의 점을 A, B L2의 두 개의 점을 C, D라 하면 

ABC = ccw(x1, y1, x2, y2, x3, y3)
ABD = ccw(x1, y1, x2, y2, x4, y4)
CDA = ccw(x3, y3, x4, y4, x1, y1)
CDB = ccw(x3, y3, x4, y4, x2, y2)

if ABC * ABD == 0 and CDA * CDB == 0:
    if isOverlap(x1, y1, x2, y2, x3, y3, x4, y4):
        print(1)
    else:
        print(0)
elif ABC * ABD <= 0 and CDA * CDB <= 0:
    print(1)
else:
    print(0)