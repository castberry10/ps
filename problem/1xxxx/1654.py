import sys
k, n = map(int, input().split()) # n -> 필요랜선 개수 
data = []
start, end = 0, 10000000
for _ in range(k):
    data.append(int(sys.stdin.readline().rstrip()))
answer = 0
while start <= end:
    temp = 0
    mid = (start + end) // 2 
    
    for i in range(k):
        temp += data[i] // mid
        
    if temp >= n:
        if mid > answer:
            answer = mid
        start = mid + 1 
        
    elif temp < n:
        end = mid - 1
    
print(answer)