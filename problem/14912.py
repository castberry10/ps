n, d = map(int, input().split())
answer = 0
d = str(d)
for i in range(1, n +1):
    data = str(i)
    for c in data:
        if c == d:
            answer += 1
            
print(answer)