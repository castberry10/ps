n, m = map(int, input().split())
data = []
for i in range(n):
    a = list(map(int, input().split()))
    data.append(a)

if n % 2== 0:
    print("YES")
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                print(data[i+1][j], end=' ')
            else:
                print(data[i-1][j], end=' ')
        print()
elif m % 2 == 0:
    print("YES")
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                print(data[i][j+1], end=' ')
            else:
                print(data[i][j-1], end=' ')
        print()
else:
    print("NO")