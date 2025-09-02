import sys
input = sys.stdin.readline

n, m = map(int, input().split())
win = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    win[a - 1] += 1
win.sort()

answer = 0
temp = -1
for i in range(n):
    if win[i] <= temp:
        answer += (temp + 1) - win[i]
        win[i] = temp + 1
    temp = win[i]

print(answer)