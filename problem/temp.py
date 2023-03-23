while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        print("AXIS")
        break 
    if x == 0 or y == 0:
        print("AXIS")
        continue
    if x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    elif x < 0:
        if y > 0:
            print("Q2")
        else:
            print("Q3")