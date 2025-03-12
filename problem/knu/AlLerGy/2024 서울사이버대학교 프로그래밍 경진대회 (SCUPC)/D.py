
n, k = map(int, input().split())
a = list(map(int, input().split()))
a2 = list(map(lambda x: (x-1)//2, a))
a3 = list(map(lambda x: x//2, a))
temp = sum(a3)
# n * k + 1
if k == 0:
    print(0)
elif temp < k:
    print(-1)
else:
    temp = sum(a2)
    if temp >= k:
        print(n+2*k-1)
    else:
        print(n+temp+k)