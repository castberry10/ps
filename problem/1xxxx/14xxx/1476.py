inputE, inputS, inputM = map(int, input().split())
# (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)
n = 1
E, S, M = 1, 1, 1

while True:
    if E == inputE and S == inputS and M == inputM:
        print(n)
        break
    n += 1
    E += 1
    S += 1
    M += 1 
    if E == 16:
        E = 1
    if S == 29:
        S = 1
    if M == 20:
        M = 1
    # print(E, S, M)