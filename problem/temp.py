cnt = 0
a = int(input())

while True:
    if a < 10:
        print(cnt)
        break
    a = str(a)
    sum = 1
    cnt += 1
    for c in a:
        sum *= int(c)
        
    a = int(sum)
    