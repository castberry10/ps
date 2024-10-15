import heapq
from collections import deque

n = int(input())
data = deque()
tempdata = []
hostqueue = [] # 힙
answer = [0] * n
for i in range(n): # 입력 순회 O(N)
    temp = list(map(int, input().split()))
    temp.append(i) # 4번째 요소는 추적 아이디
    tempdata.append(temp)

tempdata.sort(key=lambda x : x[1]) # 혹시 모르는 데이터 도착시간 정렬 O(NlogN)

for i in tempdata: # 큐에 하나씩 넣기 O(N)
    data.append(i)

# 먼저 
# 처음에 먼저 도착한 사람들을 힙에 넣음 
# 힙의 제일 먼저 나온 사람의 치료종료시간을 저장
# 치료 종료 시간까지 도착한 사람들을 힙에 넣음 
# . . . (반복   )  

currentTime = data[0][1]
while True:
    if not data and not hostqueue: # 일단 아무것도 없으면 멈춰야할테니
        break
    while True:
        if (data and currentTime < data[0][1]) or not data:
            break
        else: #  힙 추가 O(log N)을 n번 반복 -> O(NlogN)
            heapq.heappush(hostqueue, tuple(data.popleft())) # 튜플로 인한 2차 힙정렬 효과 기대 
    ## 일단 치료 시작전까지 모든 사람 도착 
    # 치료 시작 ~~ 
    score, time, needtime, id = heapq.heappop(hostqueue) # 힙 삭제 O(log N)
    # print(currentTime)
    answer[id] = currentTime
    currentTime += needtime
for i in answer: # 순회 O(N)
    print(i)


