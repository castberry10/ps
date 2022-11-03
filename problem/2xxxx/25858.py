A, B = map(int, input().split())
a = list()
for i in range(A):
    a.append(int(input()))
for i in range(A):
    print(int(B / sum(a)) * a[i])