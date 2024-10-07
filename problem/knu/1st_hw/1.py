n = int(input())
ls = [0]
ls += list(map(int, input().split()))
s = int(input())
sumls = [0] * (n + 1)

answer = [-1] * (n - s + 1)

for i in range(n):
    sumls[i + 1] = sumls[i] + ls[i + 1]
# 누적합 배열 생성 O(n)
for i in range(n - s + 1):
    temp = sumls[i + s] - sumls[i]
    if temp / s == temp // s:
        print(temp // s)
    else:
        pass