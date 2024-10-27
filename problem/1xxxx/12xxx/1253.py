n = int(input())
ls = list(map(int, input().split()))
answer = 0
ls.sort()
for i in range(n):
    l = 0
    r = n - 1
    while l < r:
        if ls[l] + ls[r] == ls[i]:
            if i == l:
                l += 1
                continue
            elif i == r:
                r -= 1
                continue
            answer += 1
            break
        elif ls[l] + ls[r] < ls[i]:
            l += 1
        elif ls[l] + ls[r] > ls[i]:
            r -= 1
print(answer)