n = int(input())
m = int(input())
ls = list(map(int, input().split()))
ls.sort()
l, r, answer = 0, 0, 0

l = 0
r = n - 1

while l < r:
    if ls[l] + ls[r] == m:
        answer += 1
        l += 1
        r -= 1
    elif ls[l] + ls[r] < m:
        l += 1
    elif ls[l] + ls[r] > m:
        r -= 1
print(answer)
