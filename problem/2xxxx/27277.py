n = int(input())
data = list(map(int,input().split()))
data.sort()
data = data[::-1]

start = 0
end = n - 1
after_data = []

while True:
    if end < start:
        break
    after_data.append(data[start])
    after_data.append(data[end])
    start += 1
    end -= 1
    

temp = 0
answer = 0 
for i in after_data:
    if temp < i:
        answer += i - temp 
    temp = i
        
print(answer)


