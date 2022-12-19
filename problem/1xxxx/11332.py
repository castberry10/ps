import math
C = int(input())

for _ in range(C):
    # S - 계산식, N - 입력 범위, T - 테스트케이스 수, L - 제한시간  
    S, N, T, L = input().split()
    N, T, L = map(int, (N, T, L))
    PC1S = 100000000
    if S == "O(N)":
        if N * T <= L * PC1S:
            print("May Pass.")
        else:
            print("TLE!")
            
    elif S == "O(2^N)":
        if (2 ** N) * T <= L * PC1S:
            print("May Pass.")
        else:
            print("TLE!")
            
    elif S == "O(N^2)":
        if (N ** 2) * T <= L * PC1S:
            print("May Pass.")
        else:
            print("TLE!")
            
    elif S == "O(N^3)":
        if (N ** 3) * T <= L * PC1S:
            print("May Pass.")
        else:
            print("TLE!")
            
    elif S == "O(N!)":
        if math.factorial(N) * T <= L * PC1S:
            print("May Pass.")
        else:
            print("TLE!")
            