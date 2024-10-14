datadic = dict()

datadic[0] = 350.34
datadic[1] = 230.90
datadic[2] = 190.55
datadic[3] = 125.30
datadic[4] = 180.90

n = int(input())

for i in range(n):
    A, B, C, D, E = map(int, input().split())
    print("$%.2f"%(A * datadic[0] + B * datadic[1] + C * datadic[2] + D * datadic[3] + E * datadic[4]))
    