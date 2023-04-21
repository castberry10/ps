import sys
n, m = map(int, input().split())
answer = 0
data = []
for _ in range(n):
    data.append(sys.stdin.readline().rstrip())
# 직사각형인줄 알아서 더럽게 짜다가 정사각형이라는 조건을 봤어요 
# 정사각형이라면 그냥 바로 조건 줄 필요없이 가로길이랑 세로 길이랑 봤으면 될텐데 말이죠 
for i in range(10):
    tempsize = 0
    size = 1
    width, height = 0, 0
    # c = 0
    tempx, tempy = -1, -1
    tempx2, tempy2 = -1, -1
    # tempsize = 0
    for y in range(n):
        for x in range(m):
            if data[y][x] == str(i):
                if tempx < 0:
                    tempx, tempy = x, y
                else: 
                    tempsize = 0
                    tempx2, tempy2 = x, y
                    if data[tempy][tempx] == data[tempy2][tempx] == data[tempy2][tempx] == data[tempy][tempx2]: 
                        width = abs(tempx - tempx2)
                        height = abs(tempy - tempy2)
                        if width == height:
                            tempsize = (width + 1) * (height + 1)
                        size = max(size, tempsize)
                
    # size = (width + 1) * (height + 1)
    answer = max(answer, size)
    
print(answer)
#저녁시간이라 보류 