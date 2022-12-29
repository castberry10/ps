import sys
n = int(input())
l = list()
for _ in range(n):
    a = int(sys.stdin.readline().strip())
    l.append(a)
l.sort(reverse = True)
for i in l:
    print(i)