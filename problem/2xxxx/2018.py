n = int(input())
start, end = 0, 0
_sum = 0
answer = 0 
while start <= n:
    if _sum == n:
        # 맞을경우
        answer += 1
        end += 1
        _sum += end 
    elif _sum < n:
        #값이 작은 경우
        end += 1
        _sum += end 

    else: # start + end > n
        #값이 클 경우
        _sum -= start
        start += 1

print(answer)