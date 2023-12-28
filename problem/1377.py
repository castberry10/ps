import sys
input = sys.stdin.readline
n = int(input())
data = []
for i in range(n):
    data.append((int(input()), i))
data.sort()

answer = 0

for i in range(n):
    # print(data[i][1], i)
    answer = max(answer, data[i][1] - i)
    
print(answer + 1)