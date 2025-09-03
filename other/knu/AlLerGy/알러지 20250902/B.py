import sys
input = sys.stdin.readline
n, m = map(int,input().split())
a  = []
for i in range(n):
    a.append(list(map(int, input().split())))


for i in range(m):
    answer = 0 
    a1, b, c = map(int, input().split())
    for j in range(n):
        # print(a[j][0], a[j][1], a1, b, c)
        if a[j][0] + a[j][1] <= a1 and a[j][0] >= b and a[j][1] >= c:
            answer += 1
    print(answer)
        