r, c = map(int, input().split())
data = {}
# [a] = [minx, miny, maxx, maxy]
n = int(input())
answer = [0, 0]
for i in range(n):
    a, y, x = map(int, input().split())
    if a not in data:
        data[a] = [x, y, x, y]
    else:
        if x < data[a][0]:
            data[a][0] = x
        elif x > data[a][2]:
            data[a][2] = x
        
        if y < data[a][1]:
            data[a][1] = y
        elif y > data[a][3]:
            data[a][3] = y
for a in sorted(data):
    dx = abs(data[a][0] - data[a][2]) + 1
    dy = abs(data[a][1] - data[a][3]) + 1
    if answer[1] < dx * dy:
        answer[0] = a
        answer[1] = dx * dy
print(answer[0], answer[1])
    
            