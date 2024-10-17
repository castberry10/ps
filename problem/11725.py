from collections import deque 
n = int(input())
tree = {}

answer = [0] * (n + 1)
for i in range(n):
    a, b = map(int, input().split())
    tree[a] = b
    tree[b] = a
queue = deque()

queue.append(1)

while queue:
    