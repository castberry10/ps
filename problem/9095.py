import sys

input = sys.stdin.readline

T = int(input())
data = [0] * 13
data[1] = 1
data[2] = 2
data[3] = 4
data[4] = 7
# . . . 
for i in range(5, 12):
    data[i] = data[i - 1] + data[i - 2] + data[i - 3]
    
for _ in range(T):
    n = int(input())
    print(data[n])