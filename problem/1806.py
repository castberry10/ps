n, s = map(int, input().split())
data = list(map(int, input().split()))
start = 0
end = 0
sum_ = data[0]
answer = 10**10
while True:
    if sum_ >= s:
        if answer > end - start:
            answer = end - start 
        start += 1
        
        sum_ -= data[start - 1]
    else: # sum_ < s
        if end == n - 1:
            break
        else: 
            end += 1 
            sum_ += data[end]



if answer == 10**10:
    print(0)
else:
    print(answer + 1)