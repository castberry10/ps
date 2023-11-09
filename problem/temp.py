n, l = map(int, input().split())
maxline = 0
maxlinecnt = 0

for i in range(n):
    precolor = ""
    templine = 0
    data = input()
    for j in range(l):
        if precolor != "1" and data[j] == '1':
            precolor = "1"
            templine += 1
        if data[j] == '0':
            precolor = '0'
    if templine > maxline:
        maxlinecnt = 1
        maxline = templine
    elif templine == maxline:
        maxlinecnt += 1
    # print(templine)
print(maxline, maxlinecnt)