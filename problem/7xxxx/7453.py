import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [],[],[],[]
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
data = {}

for i in A:
    for j in B:
        temp = i + j
        if temp not in data:
            data[temp] = 1
        else:
            data[temp] += 1
answer = 0  
for i in C:
    for j in D:
        temp = i + j
        temp = -1 * temp
        if temp in data:
            answer += data[temp]
print(answer)