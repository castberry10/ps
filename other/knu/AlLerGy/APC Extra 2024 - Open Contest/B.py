from collections import deque

n = int(input())
t = int(input())
data = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = []
q = deque(data)
for i in b:
    for j in range(i - 1):
        temp = q.popleft()
        q.append(temp)
    answer.append(q[0])
print(*answer)
        