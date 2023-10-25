import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

line = [i for i in range(101)]
visitlist = [0] * 101
queue = deque()

queue.append((1, 0))
visitlist[1] = 1
answer = 10000000
for _ in range(N+M):
    a, b = map(int, input().split())
    line[a] = b
    
##############3
# print(line)
while True:
    if len(queue) <= 0: # 큐가 비었으니 종료
        break
    x, v = queue.popleft()
    for dx in range(1, 7): # 주사위 1 ~ 6
        v += 1 # 주사위를 돌렸으니 횟수 + 1
        tempx = dx + x # 주사위 거리를 계산한 tempx 
        linex = line[tempx]
        if linex == 100: # 이게 100이면 최솟값과 비교
            answer = min(v, answer) # 
            #print(v)
            v -= 1
            break #이 이상의 주사위는 100 초과기 때문에break  
        if linex > 100:
            v -= 1
            break# 2줄 위와 동일 
         # 자기 자신 
        if visitlist[linex] == 1: # 방문했다면 
            v -= 1
            continue
        # 괜찮음
        visitlist[linex] = 1 # 안방문했으니 표시 
        queue.append((linex, v))
        v -= 1
        
print(answer)