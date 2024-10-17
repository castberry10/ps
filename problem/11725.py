from collections import deque 
import sys

input = sys.stdin.readline
n = int(input())
tree = {}

answer = [0] * (n + 1)
for i in range(n - 1):
    a, b = map(int, input().split())
    if a in tree:
        tree[a].append(b)
    else:
        tree[a] = [b]
    if b in tree:
        tree[b].append(a)
    else:
        tree[b] = [a]
queue = deque()

queue.append(1)

while queue:
    current_node = queue.popleft() # 현재 노드

    for i in tree[current_node]:
        if answer[i] == 0:
            answer[i] = current_node
            queue.append(i)
for i in range(2, n + 1):
    print(answer[i])