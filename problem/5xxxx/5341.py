while True:
    sum = 0
    a = int(input())
    if a == 0:
        break 
    for i in range(1, a+1):
        sum += i
    print(sum)