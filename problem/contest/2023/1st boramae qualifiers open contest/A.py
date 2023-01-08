n = int(input())

a = list(map(int, input().split()))

answer = 0
for i in range(3):
    if a[i] >= n:
        answer += n
    else:
        answer += a[i]
        
print(answer)