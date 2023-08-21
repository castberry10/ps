n, k = map(int, input().split())

data = []
answer = 0

for i in range(n):
    data.append(int(input()))

data = data[::-1]

for i in data:
    answer += k // i
    k = k % i
    if k == 0:
        break
        
print(answer)

