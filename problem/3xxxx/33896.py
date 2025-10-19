n = int(input())

data = []
for i in range(n):
    n, s, r, c=  input().split()
    s, r, c = map(int, (s, r, c))
    
    a = (s ** 3) / (c * (r + 1))
    a = int(a)
    data.append(list((n, a, c)))
# print(data)
data.sort(key=lambda x: (-x[1], x[2], x[0]))
# print(data)
print(data[1][0])
    

    