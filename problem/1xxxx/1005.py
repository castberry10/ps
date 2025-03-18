import sys
from collections import deque

input = sys.stdin.readline
def solve():
    n, k = map(int, input().split())
    D = list(map(int,input().split()))
    g = {}
    memo = [0] * n
    answerlist = [0] * n
    for i in range(k):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if x not in g:
            g[x] = []
        g[x].append(y)
        memo[y] += 1

    last = int(input())
    last -= 1
    queue = deque()

    for i in range(n):
        if memo[i] == 0:
            queue.append(i)
            answerlist[i] = D[i]

    while queue:
        cur = queue.popleft()
        if cur in g:
            for next in g[cur]:
                memo[next] -= 1
                answerlist[next] = max(answerlist[next], answerlist[cur] + D[next])
                if memo[next] == 0:
                    queue.append(next)
    print(answerlist[last])
                    
        
t = int(input())

for i in range(t):
    solve()