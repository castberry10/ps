import copy
n = int(input())
data = list(input().split())
d1 = {'B' : 5,'S' : 4,'G' : 3,'P' : 2,'D' : 1}
c = 0
data1 = copy.deepcopy(data)
for _ in range(n):
    for i in range(n - 1):
        if d1[data1[i][0]] < d1[data1[i+1][0]]:
            data1[i+1], data1[i] = data1[i], data1[i + 1]
            c = 1
        elif data1[i][0] == data1[i+1][0] and int(data1[i][1:]) < int(data1[i + 1][1:]):
            data1[i+1], data1[i] = data1[i], data1[i + 1]
            c = 1
            
if c == 0:
    print('OK')
else:
    print('KO')
    c = 0
    
    for i in range(n):
        if data[i] != data1[i]:
            if c == 0: 
                c = 1
                a = data1[i]
            else:
                
                b = data1[i]
    print(a, b)