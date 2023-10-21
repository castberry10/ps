import sys
input = sys.stdin.readline
n = int(input())
data = list()
for i in range(n):
    data.append(int(input()))
data.sort()
for i in data:
    print(i)