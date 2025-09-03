n, m = map(int, input().split())
data = [input() for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1),
        (-1, -1), (-1, 1), (1, -1), (1, 1)]

answer = 0
for i in range(n):
    for j in range(m):
        if data[i][j] != 'F':
            continue
        for dx, dy in dxy:
            x1, y1 = i + dx, j + dy
            x2, y2 = i + 2*dx, j + 2*dy
            if 0 <= x1 < n and 0 <= y1 < m and 0 <= x2 < n and 0 <= y2 < m:
                if data[x1][y1] == 'O' and data[x2][y2] == 'X':
                    answer += 1

print(answer)
