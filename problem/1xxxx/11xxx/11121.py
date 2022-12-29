n = int(input())
for _ in range(n):
    s1, s2 = input().split()
    if s1 == s2:
        print('OK')
    else:
        print('ERROR')