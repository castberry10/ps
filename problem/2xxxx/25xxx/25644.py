n = int(input())
nlist = list(map(int, input().split()))

answer = 0
point = 0
min_ = 1e9

while True:
    if point == n:
        break 
    if min_ > nlist[point]: #작은 값 갱신 
        min_ = nlist[point]
        point += 1
        continue
    elif min_ < nlist[point]:# 차이 발생 
        temp = nlist[point] - min_
        if temp > answer:
            answer = temp
        point += 1
            
print(answer)
        
    
    