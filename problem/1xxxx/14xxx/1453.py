a = [0]*105
n = int(input())
data = list(map(int, input().split()))
answer = 0
for i in data:
    if a[i] == 0:
        a[i] = 1
    else:
        answer += 1
print(answer)