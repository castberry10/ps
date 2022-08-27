import sys
N = int(input())

for _ in range(int(N)):
    a, b = sys.stdin.readline().split()
    print(int(a) + int(b))