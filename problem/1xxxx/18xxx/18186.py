#그리디 문제 
# 5 3 2
# 1 1 1 0 2 - > 13
# 1 1 1 -> 7 <- 3 + 2 * 2
# 1 1 -> 5 <- 3 + 2
# 1 -> 3 
n, b, c = map(int, input().split())
# b = b
bc = b + c
b2c = b + 2 * c
a = list(map(int, input().split())) #a의 범위는 n 

answer = 0
if b <= c: #b가 c보다 작다면 굳이 계산 필요 x 
    answer = sum(a) * b
    print(answer)
    exit()

for i in range(n - 2):
    if a[i + 1] > a[i + 2]:
        minbc = min(a[i + 1] - a[i + 2], a[i])
        
        # print(a, 5, i)
        answer += bc * minbc
        a[i] -= minbc
        a[i + 1] -= minbc
        
    if a[i] > 0 and a[i + 1] > 0 and a[i + 2] > 0:
        minb2c = min(a[i], a[i + 1], a[i + 2])
        # print(a, 7, i)
        a[i + 0] -= minb2c
        a[i + 1] -= minb2c
        a[i + 2] -= minb2c
        answer += b2c * minb2c
    

if a[n - 2] > 0:
    if a[n - 1] >0:
        minbc = min(a[n-1], a[n-2])
        # print(a, 5, n-2)
        answer += bc * minbc
        a[n-2] -= minbc
        a[n-1] -= minbc

for i in range(n):
    answer += b * a[i]
    
# print(a, 3)
print(answer)