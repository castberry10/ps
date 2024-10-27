data = [0] * 70
data[0] = 1
data[1] = 1
data[2] = 2
data[3] = 4
for i in range(4, 68):
    data[i] = data[i-1] + data[i-2] + data[i-3] + data[i-4]
    
n = int(input())
for i in range(n):
    a = int(input())
    print(data[a])