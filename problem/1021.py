from collections import deque


n, m = map(int, input().split())
inputdata = list(map(int, input().split()))
data = list(range(1, n+1))
deque = deque(data)
answer = 0

# 1 2 3 4 5
#  3 
for i in inputdata:
    while True: 
        iindex = deque.index(i)
        if iindex == 0:
            deque.popleft()
            break
        if iindex <= len(deque) // 2:
            deque.rotate(-1)
            answer += 1
        else:
            deque.rotate(1)
            answer += 1
print(answer)
            