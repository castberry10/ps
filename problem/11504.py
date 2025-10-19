import sys

input = sys.stdin.readline
answer = 0
while True:
    n = int(input())
    treelist = []
    answer = 0
    if n == 0:
        break
    w, h = map(int, input().split())
    grid = [[0]*(w+1) for _ in range(h+1)]
    for _ in range(n):
        x, y = map(int, input().split())
        grid[y][x] += 1
    st = list(map(int, input().split()))

    S, T = st[0], st[1] 

    for y1 in range(1, h - T + 2):       
        for x1 in range(1, w - S + 2):   
            cnt = 0
            for y in range(y1, y1 + T):
                for x in range(x1, x1 + S):
                    cnt += grid[y][x]
            if cnt > answer:
                answer = cnt

    print(answer)