n, m = map(int, input().split())
answer = 0
for _ in range(n):
    data = input()
    if data.count('O') > m // 2:
        answer += 1
print(answer)