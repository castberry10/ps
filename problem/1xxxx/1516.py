import sys 
from collections import deque
input = sys.stdin.readline
queue = deque()
n = int(input())
grape = {}
indegree = [0] * n
answer = [0] * n
time = [0] * n

for i in range(n):
    data = list(map(int, input().split()))
    data_len = len(data) - 1
    time[i] = data[0]
    indegree[i] = data_len - 1
    if data_len - 1 == 0:
        queue.append(i)
    for j in range(1, data_len, 1):
        if data[j] - 1 not in grape:
            grape[data[j] - 1] = []
        grape[data[j] - 1].append(i)

sorttable = []
while queue:
    print(queue)
    temp = queue.popleft()
    answer[temp] += time[temp]
    if temp in grape:
        for i in grape[temp]:
            indegree[i] -= 1
            answer[i] = max(answer[i], answer[temp])
            if indegree[i] == 0:
                queue.append(i)
for i in answer:
    print(i)