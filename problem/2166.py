import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
data.append(data[0])

answer = 0.0

for i in range(n):
    answer += (data[i][0]*data[i+1][1] - data[i+1][0]*data[i][1])
    
answer = abs(answer / 2.0)
print(round(answer,1))