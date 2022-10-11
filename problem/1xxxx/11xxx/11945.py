n, m = map(int, input().split())
a = []

for i in range(n):
    a.append(input())

for i in a:
    print(i[::-1])