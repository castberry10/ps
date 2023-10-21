n = int(input())
data = list(map(int, input().split()))
data += [0,0,0,0]
answer = 0
if data[0] > data[2]:
    answer += (data[0] - data[2]) * 508
else:
    answer += (data[2] - data[0]) * 108
    
if data[1] > data[3]:
    answer += (data[1] - data[3]) * 212
else:
    answer += (data[3] - data[1]) * 305
    
if n == 5:
    answer += (data[4] * 707)
    
print(answer * 4763)
    