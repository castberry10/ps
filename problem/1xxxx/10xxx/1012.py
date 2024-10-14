from collections import deque
import sys

input = sys.stdin.readline
queue = deque()
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
T = int(input())
# 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 
# 그 다음 줄부터 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 
# 배추밭의 가로길이 M(1 ≤ M ≤ 50)과 세로길이 N(1 ≤ N ≤ 50), 그리고 배추가 심어져 있는 위치의 개수 K(1 ≤ K ≤ 2500)이 주어진다. 
# 그 다음 K줄에는 배추의 위치 X(0 ≤ X ≤ M-1), Y(0 ≤ Y ≤ N-1)가 주어진다. 두 배추의 위치가 같은 경우는 없다.
for _ in range(T):
    M, N, K = map(int, input().split())
    mapdata = [[0 for _ in range(M)] for _ in range(N)]
    visitdata = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        mapdata[Y][X] = 1
        queue.append((Y, X))
    while True:
        if len(queue) == 0:
            break
        y, x = queue.pop()
        if visitdata[y][x] == 0 and mapdata[y][x] == 1:
            answer += 1
        for dy, dx in dxy:
            if 0 <= y + dy < N and 0 <= x + dx < M and mapdata[y+dy][x+dx] == 1 and visitdata[y+dy][x+dx] == 0:
                visitdata[y+dy][x+dx] = 1
                queue.append((y+dy, x+dx))
    print(answer)
                