while True:
    l = list(map(int, input().split()))
    l.sort()
    
    if l[0] == l[1] == l[2] == 0:
        break
    if l[0] * l[0] + l[1] * l[1] == l[2] * l[2]:
        print('right')
    else:
        print('wrong')