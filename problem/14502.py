from collections import deque

dx = [-1, 1 , 0 , 0]
dy = [0, 0, -1, 1]

    
queue = deque()
answer = 0

N , M = map(int, input().split()) #N -> 세로 길이 #M 가로 길이 

baseMap = [list(map(int,input().split())) for _ in range(N)]

testMap = [[0 for _ in range(m)] for _ in range(n)]



def bfs(): #검증
    for n in range(N):
        for m in range(M):
            testMap[x][y] = baseMap[x][y]
    
            
def bt(select): #backTracking
    if select == 3: 
        return;
    for n in range(N):
        for m in range(M):
            if baseMap[n][m] == 1:
                continue
            baseMap[n][m] = 1
            bt(select + 1)
            baseMap[][] = 0


# for x in range(n):
#     for y in range(m):
#             

bt(0)
