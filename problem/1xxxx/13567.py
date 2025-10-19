n, m = map(int, input().split())
cx, cy = 0, 0
d = 0
dxy = [[1,0], [0,-1], [-1,0], [0,1]]
answer = 0
for i in range(m):
    a, b = input().split()
    b = int(b)
    if a == "MOVE":
        cx += dxy[d][0] * b
        cy += dxy[d][1] * b
        if not (0 <= cx < n) or (not 0 <= cy < n):
            answer = -1
    elif a == "TURN":
        if b:
            if d == 3:
                d = 0
            else:
                d += 1
        else: 
            if d == 0:
                d = 3
            else:
                d -= 1
if answer == -1:
    print(answer)
else:
    print(cx, cy)