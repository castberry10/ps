from collections import deque
import sys
queue = deque()
q = deque()
answer = ""
temp = 0 
n = int(input())
for _ in range(n):
    input_ = sys.stdin.readline()
    if input_[0] == '1':
        q.append(1)
        queue.append(input_[2])
    elif input_[0] == '2':
        q.append(2)
        queue.appendleft(input_[2])
    else:
        if q:
            pass
        else:
            continue
        temp = q.pop()
        if temp == 1:
            queue.pop()
        else: # 2
            queue.popleft()

if queue:
    print(*queue, sep = "")
else:
    print(0)
