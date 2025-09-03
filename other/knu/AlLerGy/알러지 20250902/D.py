n = int(input())
data = []
answer = 0
for i in range(n):
    data.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        for i2 in range(n):
            if i <= i2:
                continue
            for j2 in range(n):
                if j <= j2:
                    continue
                temp = []
                for it in range(i, i2+1):
                    for jt in range(j, j2 +1):
                        temp.append(data[it][jt])
                print(temp, list(range((i2 - i) * (j2-j))))
                if temp == list(range((i2 - i) * (j2-j))):
                    answer += 1
print(answer)

# n = int(input().strip())
# data = [list(map(int, input().split())) for _ in range(n)]

# answer = 0
# for i in range(n):
#     for j in range(n):
#         for i2 in range(i, n):      
#             for j2 in range(j, n): 
#                 temp = set()
#                 tof = True
#                 for it in range(i, i2 + 1):
#                     for jt in range(j, j2 + 1):
#                         v = data[it][jt]
#                         if v in temp:
#                             tof = False
#                             break
#                         temp.add(v)
#                     if not tof:
#                         break
#                 if tof:
#                     answer += 1

# print(answer)

