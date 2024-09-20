N = int(input())

data = []

for i in range(N):
    temp = list(input().split())
    # data.append()
    temp[1], temp[2], temp[3] = map(int,(temp[1], temp[2], temp[3]))
    data.append(temp)
    
data.sort(key = lambda x : ( - x[1], x[2], -x[3], x[0]))
# for i in data:
#     for j in i:
#         print(i, end = " ")
#     print()
for i in data:
    print(i[0])
    
    