def solve():
    n = int(input())
    s = input()
    num1 = 0
    for i in s:
        if '1' == i:
            num1 += 1
    num0 = n - num1
    answer = num1 * n + num0 - num1
    print(answer)
t = int(input())
for T in range(t):
    solve()