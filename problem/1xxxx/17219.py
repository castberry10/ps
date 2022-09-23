import sys
N, M = map(int, input().split())
passwd = {}
for i in range(N):
    a = sys.stdin.readline().rstrip().split()
    passwd[a[0]] = a[1]
for i in range(M):
    a = sys.stdin.readline().rstrip()
    print(passwd[a])