n = int(input())
cx, cy, hx, hy, status = 0,-1, 0,0,0
for i in range(n):
    data = input()
    if data == 'W':
        if status == 0:
            cy += 1
            hy += 1
        elif status == 1:
            cx += 1
            hx += 1
        elif status == 2:
            cy -= 1
            hy -= 1
        else:
            cx -= 1
            hx -= 1
    if data == "A":
        if status == 0:
            cx -= 1
            hx -= 1
        elif status == 1:
            cy += 1
            hy += 1
        elif status == 2:
            cx += 1
            hx += 1
        else:
            cy -= 1
            hy -= 1
    if data == "S":
        if status == 0:
            cy -= 1
            hy -= 1
        elif status == 1:
            cx -= 1
            hx -= 1
        elif status == 2:
            cy += 1
            hy += 1
        else:
            cx += 1
            hx += 1
    if data == "D":
        if status == 0:
            cx += 1
            hx += 1
        elif status == 1:
            cy -= 1
            hy -= 1
        elif status == 2:
            cx -= 1
            hx -= 1
        else:
            cy += 1
            hy += 1
    if data == "MR":
        if status == 0:
            cx = hx - 1
            cy = hy
        elif status == 1:
            cx = hx
            cy = hy + 1
        elif status == 2:
            cx = hx + 1
            cy = hy
        else:
            cx = hx
            cy = hy - 1
        status += 1
        status = status % 4
        
    if data == "ML":
        if status == 0:
            cx = hx + 1
            cy = hy
        elif status == 1:
            cx = hx
            cy = hy - 1
        elif status == 2:
            cx = hx - 1
            cy = hy
        else:
            cx = hx
            cy = hy + 1
        status -= 1
        if status == -1:
            status = 3
    print(hx, hy, cx, cy)