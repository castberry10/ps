from itertools import permutations

def solve():
    n,x = map(int, input().split())
    answer = []
    if n == 1:
        print(0)
        return
    if x == 0:
        for i in range(1, n):
            answer.append(i)
        answer.append(0)
    else:
        for i in range(0, x):
            answer.append(i)
        for i in range(x+1, n):
            answer.append(i)
        if n != x:
            answer.append(x)
    print(*answer)
t = int(input())
for T in range(t):
    solve()