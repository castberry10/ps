import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = []

for i in range(N):
    A, B = map(int, input().split())
    temp = B - A
    data.append(temp)
data.sort()
pluscnt = 0
print(data)
for i in range(N):
    if data[i] > 0:
        point = i - 1
        break
        # cnt += i - 1
while True:
    # print(point)
    if point >= K:
        break
    for i in range(point, len(data)): # point는 가르키는 인덱스
        if data[i] > data[point]: #data[i] 가르키는 인덱스의 값  
            print(data[i], data[point], pluscnt, i, point)
            pluscnt = data[i]
            point = i

print(pluscnt)