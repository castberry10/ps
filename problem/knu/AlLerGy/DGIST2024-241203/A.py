a = list(map(int, input().split()))
b = list(map(int,input().split()))

def summ(x):
    return x[0] * 13 + x[1] * 7 + x[2] * 5 + x[3] * 3 + x[4] * 3 + x[5] * 2
a = summ(a)
b = summ(b) + 1.5

if a < b:
    print("ekwoo")
else:
    print("cocjr0208")