x1, y1, x2, y2, x3, y3 = map(int, input().split())

# ab
# cd - > a * b - c * d
def ccw(x1, y1, x2, y2, x3, y3):
    return (x3-x2)*(y2-y1) - (y3-y2) * (x2 - x1)

if ccw(x1, y1, x2, y2, x3, y3) == 0:
    print(0)
elif ccw(x1, y1, x2, y2, x3, y3) > 0:
    print(-1)
else:
    print(1)