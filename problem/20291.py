import sys

input = sys.stdin.readline

n = int(input())
data = dict()
# dataset = []
for _ in range(n):
    a, b = input().split(".")
    if b in data:
        data[b] += 1
    else:
        data[b] = 1

dataset = list(data.keys())
dataset.sort()

for i in dataset:
    print(i, data[i])