
target = []
nexttarget = []
n, m = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())
    target.append([x, y])
for i in range(m):
    x, y = map(int, input().split())
    nexttarget.append([x, y])

answer = 0
x, y = 0, 0
tempx = 0
tempy = 0
for i in range(m):
    dist = 0
    distindex = -1
    for j in range(n): # 가장 먼 과녁 찾기
        tempdist = (target[j][0]- x) ** 2 + (target[j][1]- y) ** 2
        if dist < tempdist:
            tempx = target[j][0]
            tempy = target[j][1]
            dist = tempdist
            distindex = j
    answer += dist
    del target[distindex]
    x = tempx
    y = tempy
    target.append(nexttarget[i])
print(answer)
        