a, b = map(int, input().split())
k, x = map(int, input().split()) # k - 
aset = set(range(a, b+1))

bset = list(range(k-x, x + k + 1))

answer = 0
for i in bset:
    if i in aset:
        answer += 1

if answer > 0:
    print(answer)
else:
    print('IMPOSSIBLE')