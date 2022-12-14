n,m,b = map(int, input().split())
data = list()
b1 = b

answer1, answer2 = 9999999999999, 0
for _ in range(n):
    data += list(map(int, input().split()))
data.sort()
data = data[::-1]
min_, max_ = data[-1], data[0]
for i in range(min_, max_ + 1):
    temp = 0
    b=b1
    tof = True
    for index in range(len(data)):
        if i < data[index]: #캐야함
            temp += (data[index] - i) * 2
            b += data[index] - i
            
        if i > data[index]: # 채워야함
            if b >= i - data[index]: #인벤토리에 있음 
                b -= i - data[index]
                temp += i - data[index]
            else:
                tof = False
                break
                
    if tof == False: #자재 부재의 이유로 종료된 경우 케이스에서 제외 
        continue
        
    if temp <= answer1:
        answer1 = temp
        answer2 = i
    # print(answer1, answer2)

print(answer1, answer2)
# print(data)