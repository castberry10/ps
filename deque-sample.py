from collections import deque

queue = deque()

N = int(input())

for i in range(1, N + 1):
    queue.append(i)
# print(queue)
while True:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
    # print(queue)
    if len(queue) == 1:
        break

print(queue.pop())
