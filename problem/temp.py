data = []

for i in range(int(input())):
    data = list(map(int, input().split()))
    data.sort()
    print(data[7])