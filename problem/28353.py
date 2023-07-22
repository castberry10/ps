n, k = map(int, input().split())
data = list(map(int, input().split()))
p1, p2 = 0, n - 1

data.sort()
answer = 0
#p1이 작은쪽 p2가 큰쪽
while p1 < p2:
    if data[p1] + data[p2] <= k:
        p1 += 1
        p2 -= 1
        answer += 1
    else:
        p2 -= 1
    
print(answer)
