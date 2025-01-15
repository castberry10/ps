n = int(input())
data = list(map(int, input().split()))
ch = True
while True:
    if ch == False:
        break
    ch = False
    s = sum(data)
    s = -s
    for i in range(n):
        if s > data[i]:
            data[i] = s
            ch = True
            break
print(sum(data))