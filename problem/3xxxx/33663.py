h1, h2 = map(int,input().split())
s1, s2 = map(int,input().split())
v1, v2 = map(int,input().split())
r, g, b = map(int,input().split())
m = min((r, g, b))
M = max((r, g, b))
V = M
S = 255 * (V - m) / V
if V == r:
    H = 60 * (g-b) / (V-m)
if V == g:
    H = 120 + (60 * (b- r))/(V-m)
if V == b: 
    H = 240 + (60 * (r-g)) / (V-m)
if H < 0:
    H = H + 360
elif H > 360:
    H = H - 360
# print(H, S, V)
if h1 <= H <= h2 and v1 <= V <= v2 and s1 <= S <= s2:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")