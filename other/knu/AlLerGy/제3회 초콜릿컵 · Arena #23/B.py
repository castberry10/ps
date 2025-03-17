t = int(input())
def solve():
    n = int(input())
    if n == 1 :
        print(0)
    else: 
        print("1" + "2" * (n-2) + "1")
for i in range(t):
    solve()