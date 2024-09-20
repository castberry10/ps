n = int(input())
data = list()

for i in range(n):
    data.append(int(input()))

data.sort()
data.reverse()

# len(data) == 7 이라면 temp == 2
temp = n // 3

answer = 0

for i in range(temp):
    tempanswer = data[i * 3] + data[i * 3 + 1] + data[i * 3 + 2]
    tempanswer -= min(data[i * 3] , data[i * 3 + 1] , data[i * 3 + 2])
    answer += tempanswer

for i in range(temp * 3, n):
    answer += data[i]

print(answer)