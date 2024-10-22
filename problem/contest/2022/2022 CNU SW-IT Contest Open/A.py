b, p = map(int, input().split())
answer = 0

while True:
    if b >=2  and p >=1:
        b -= 2
        p -= 1
        answer += 1
    else:
        break
print(answer)