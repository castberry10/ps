n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
cnt = 0
for i in range(n):
    # cnt += a[i] - b[i]
    if a[i] < b[i]:
        cnt += b[i] - a[i]
    else:
        cnt += a[i] - b[i]
cnt = abs(cnt)
print(cnt // 2)