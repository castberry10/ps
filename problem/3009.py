xdata = list()
ydata = list()
for _ in range(3):
    x, y = map(int, input().split())
    xdata.append(x)
    ydata.append(y)

for i in range(3):
    if xdata.count(xdata[i]) == 1:
        xp = xdata[i]
    if ydata.count(ydata[i]) == 1:
        yp = ydata[i]

print(xp, yp)