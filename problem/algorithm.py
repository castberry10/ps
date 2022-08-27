from collections import deque

dx = [-1, 1 , 0 , 0]
dy = [0, 0, -1, 1]

def bfs(): #검증
    global answer
    testzerocount = 0
    visitMap = [[0 for _ in range(10)] for _ in range(10)]
    for x in range(n):
        for y in range(m):
            testMap[x][y] = baseMap[x][y]
            if testMap[x][y] == 2:
                queue.append([x,y])
                

    
    while(queue):
        x, y = queue.popleft() #.split()
        visitMap[x][y] = 1
        for i in range(4):#상 하 좌 우 느낌 
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m: #if testMap[x+dx[i]][y+dy] -< overflow 
                if visitMap[x+dx[i]][y+dy[i]] == 0 and testMap[x+dx[i]][y+dy[i]] == 0: # 방문하지 않고, 빈 공간이면 
                    queue.append([x+dx[i], y+dy[i]])
                    testMap[x+dx[i]][y+dy[i]] = 2
                    visitMap[x+dx[i]][y+dy[i]] = 1
                    
                    
                    
    # for i in range(len(testMap)):           
    # 	for j in range(len(testMap[i])):     
    #     	print(testMap[i][j], end=' ')
    # 	print()
    for x in range(n):
        for y in range(m):
            if testMap[x][y] == 0:
                testzerocount = testzerocount + 1 
                # print(testzerocount)
                
                
    
    if testzerocount > answer:
        answer = testzerocount
            
def bt(select): #backTracking
    global cnt
    cnt += 1
    if select == 3: # 다 선택하면
        bfs()
        return
    # print(select)
    for x in range(n):
        for y in range(m):
            if selectMap[x][y] == 0 and baseMap[x][y] == 0:
                # selectMap[x][y]==1
                baseMap[x][y] == 1
                bt(select + 1)
                
                # baseMap[x][y] == 0
                selectMap[x][y]==0
    
queue = deque()
answer = 0


n , m = map(int, input().split())

baseMap = [list(map(int,input().split())) for _ in range(n)]
testMap = [[0 for _ in range(n)] for _ in range(m)]

visitMap = [[0 for _ in range(n)] for _ in range(m)]
selectMap = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0
for x in range(n):
    for y in range(m):
            testMap[x][y] = baseMap[x][y]
testMap = [[0 for _ in range(n)] for _ in range(m)]
# for i in range(len(baseMap)):            
#     for j in range(len(baseMap[i])):    
#         print(baseMap[i][j], end=' ')
#     print()
# for i in range(len(testMap)):           
#     for j in range(len(testMap[i])):     
#         print(testMap[i][j], end=' ')
#     print()
bt(0)
print(cnt)
print(answer) 
