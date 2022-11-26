from collections import deque
maxn = 0
n = int(input())
queue = deque()

for _ in range(n):
    st = input()
    for c in st:
        queue.append(c)
        #푸는 중 