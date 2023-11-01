import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n1 = int(input())
    data1 = set(map(int, input().split()))
    n2 = int(input())
    data2 = list(map(int, input().split()))
    for i in data2:
        if i in data1:
            print(1)
        else:
            print(0)
