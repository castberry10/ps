from collections import deque
##
A, B = map(int, input().split())

# A를 B로만들기 
# 1. 2를곱하거나 
# 2. 숫자 뒷 자리에 1을 추가 (숫자 * 10 + 1)

queue = deque()

# queue = de
queue.append((A, 1))

while True:
    if len(queue) == 0:
        print(-1)
        break
    tempA, tempCnt = queue.popleft()
    if tempA > B:
        continue
    if tempA == B:
        print(tempCnt)
        break
    queue.append((tempA*2, tempCnt + 1))
    queue.append((tempA*10 + 1, tempCnt + 1))
    
# answer = 0 
