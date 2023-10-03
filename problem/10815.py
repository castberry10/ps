n = int(input())
dataset = set(map(int,input().split()))
m = int(input())
data = list(map(int, input().split()))

for i in data:
    if i in dataset:
        print(1, end = ' ')
    else:
        print(0, end = ' ')