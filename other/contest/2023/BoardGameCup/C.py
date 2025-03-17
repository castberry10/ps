n = int(input())
reverseTimeValue = -1
currentTime = 1 
for _ in range(n):
    s, x = input().split()
    x = int(x)
    if s == "WATCH" or s == "CLOCK": # 벽시계 또는 손목시계 
        if currentTime  == x:
            print(currentTime, "YES")
        else:
            print(currentTime, "NO")
            
    elif s == "HOURGLASS":# 모래시계
        if currentTime == x:
            print(currentTime, "NO")
        else:
            reverseTimeValue *= -1
            print(currentTime, "NO")
    if reverseTimeValue == -1:
        currentTime += 1
        if currentTime == 13:
            currentTime = 1
    else:
        currentTime -= 1 
        if currentTime == 0:
            currentTime = 12
        