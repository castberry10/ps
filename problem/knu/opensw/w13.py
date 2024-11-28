n = int(input())
data = []
def sortfunc(a):
    a1, b2, c3 = a
    return (-b2, c3)

for i in range(n):
    a, b, c = input().split()
    b = int(b)
    data.append(tuple((a, b, c)))

data.sort(key=sortfunc)
for a, b, c in data:
    print(a)
