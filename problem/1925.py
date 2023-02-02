a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
#x y 
#x y 
#x y
l1 = (a1 - b1) ** 2 + (a2 - b2) ** 2
l2 = (c1 - b1) ** 2 + (c2 - b2) ** 2
l3 = (a1 - c1) ** 2 + (a2 - c2) ** 2

l123 = list((l1, l2, l3))
l123.sort()
x1, x2, x3 = a1, b1, c1 
y1, y2, y3 = a2, b2, c2 

s = (x1 * y2 + x2 * y3 + x3 * y1) - (x1 * y3 + x3 * y2 + x2 * y1)
if a1 == b1 == c1 or a2 == b2 == c2 or s == 0:
    print("X")
elif (a1 - b1) ** 2 + (a2 - b2) ** 2 == (c1 - b1) ** 2 + (c2 - b2) ** 2 == (a1 - c1) ** 2 + (a2 - c2) ** 2:
    print("JungTriangle")
elif l1 == l2 or l2 == l3 or l3 == l1:
    if l123[2] == l123[0] + l123[1]:
        print("Jikkak2Triangle")
    elif l123[2] > l123[1] + l123[0]:
        print("Dunkak2Triangle")
    else:
        print("Yeahkak2Triangle")
else:
    if l123[2] == l123[0] + l123[1]:
        print("JikkakTriangle")
    elif l123[2] > l123[1] + l123[0]:
        print("DunkakTriangle")
    else:
        print("YeahkakTriangle")