import sys
n, m = map(int,input().split())
data = list(map(int,input().split()))
prefixSumList = [0] * n
prefixSumList[0] = data[0]
for i in range(1, n):
    prefixSumList[i] += data[i] + prefixSumList[i - 1]
# print(prefixSumList)
for _ in range(m):
    i1, i2 = map(int, sys.stdin.readline().split())
    i1, i2 = i1 - 1, i2 - 1
    if i1 == 0:
        print(prefixSumList[i2])
    else:
        print(prefixSumList[i2] - prefixSumList[i1 - 1])
        
    