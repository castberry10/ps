import sys

input = sys.stdin.readline

T = int(input())
data0 = [0] * 45
data1 = [0] * 45

data0[0] = 1
data1[0] = 0
data0[1] = 0
data1[1] = 1

for i in range(2, 42):
    data0[i] = data0[i - 1] + data0[i - 2]
    data1[i] = data1[i - 1] + data1[i - 2]

for _ in range(T):
    n = int(input())
    print(data0[n], data1[n])