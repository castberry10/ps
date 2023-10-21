n = int(input())
data1 = list(map(int, input().split()))
data2 = sorted(data1)
answer = 0 
for i in range(n):
    if data1[i] != data2[i]:
        answer += 1
print(answer)