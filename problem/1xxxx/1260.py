s1 = {}
s2 = {}
N, M = map(int, input().split())
for i in range(N):
    s1[i + 1] = input()

s2 = {v:k for k,v in s1.items()}
for i in range(M):
    a = input()
    if a.isnumeric():
        print(s1[int(a)])
    else:
        print(s2[a])