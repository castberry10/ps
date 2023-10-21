n = int(input())
answer = 0
applecnt = 0
for i in range(n):
    T, W, H, L = input().split()
    W, H, L = map(int, (W, H, L))
    if T == 'A':
        apple = (W // 12) * (H // 12) * (L // 12)
        answer += 1000 + apple * 500
        applecnt += apple
    if T == 'B':
        answer += 6000
print(answer)
print(applecnt * 4000)