def gcd(a, b):
    if a < b:
        a, b = b, a
    # a가 크다
    while True:
        if a % b == 0:
            return b
        else:
            a, b = b, a % b
        
n = int(input())
data = list(map(int, input().split()))
for i in range(1, n):
    tempgcd = gcd(data[0], data[i])
    print('%s/%s' % (data[0]//tempgcd, data[i]//tempgcd))