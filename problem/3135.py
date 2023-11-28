import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
btn = []
for i in range(n):
    btn.append(int(input()))

mindata = abs(a - b)
minindex = -1
answer = 0

for i in range(n):
    if mindata > abs(btn[i] - b):
        mindata = abs(btn[i] - b)
        minindex = i
        # print(minindex, mindata)

if minindex == -1:
    pass
else:
    answer = 1
    a = btn[minindex]
# print(btn)
# print(answer, a, b)
print(answer + abs(a - b))