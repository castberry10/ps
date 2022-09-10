import sys
N = int(input())
sortls = [0] * 10002

for i in range(N):
    a = int(sys.stdin.readline())
    sortls[a] += 1

for i in range(1,N + 1):
    for _ in range(sortls[i]):
        print(i)