from collections import deque

dx = [-1, 1 , 0 , 0]
dy = [0, 0, -1, 1]

    
queue = deque()
answer = 0

N , M = map(int, input().split()) #N -> 세로 길이 #M 가로 길이 

baseMap = [list(map(int,input().split())) for _ in range(N)]

testMap = [[0 for _ in range(M)] for _ in range(N)]


def bfs(): #검증
    global answer
    
    temp = 0 # 임시 answer
    
    #bfs 대상 찾기 
    for n in range(N):
        for m in range(M):
            testMap[n][m] = baseMap[n][m]
            if testMap[n][m] == 2:
                queue.append([n, m])
    #바이러스 퍼트리기 
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N: #index로 부터 안전
                if testMap[y+dy[i]][x+dx[i]] == 0:
                    queue.append([y+dy[i],x+dx[i]])########## 방문한곳에 대한 문제 발생 
                    testMap[y+dy[i]][x+dx[i]] = 2 #반복이 계속되지않도록 
                    
    #감염 안된 구역 카운트 
    for n in range(N):
        for m in range(M):
            if testMap[n][m] == 0:
                temp += 1 #################
                
    if temp > answer:
        answer = temp
    
def bt(select): #backTracking
    if select == 3: 
        bfs()
         
        return;
    for n in range(N):
        for m in range(M):
            if baseMap[n][m] != 0:
                continue
            baseMap[n][m] = 1
            bt(select + 1)
            baseMap[n][m] = 0


# for x in range(n):
#     for y in range(m):
#             

bt(0)
print(answer)