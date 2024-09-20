import sys

input = sys.stdin.readline
n, m = map(int, input().split())

ndata = []
mdata = []

for i in range(n):
    ndata.append(input().rstrip())
for i in range(m):
    mdata.append(input().rstrip())

ndata = set(ndata)

answer = []

for i in mdata:
    if i in ndata:
        answer.append(i)
answer.sort()

print(len(answer))
for i in answer:
    print(i)