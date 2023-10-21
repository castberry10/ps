data = list(map(int, input().split()))
answer = 0
for i in data:
    if i > 0:
        answer += 1
print(answer)