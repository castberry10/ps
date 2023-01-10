import sys 
n = int(input())

sum_ = 0
xor_ = 0
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 1:
        sum_ += data[1]
        xor_ ^= data[1]
    elif data[0] == 2:
        sum_ -= data[1]
        xor_ ^= data[1]
    elif data[0] == 3:
        print(sum_)
    elif data[0] == 4:
        print(xor_)