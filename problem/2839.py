# import time
N = int(input())
answer = 0 

while N:
    if N % 5 == 0:
        answer += N // 5
        break 
    elif N >= 3:
        answer += 1
        N -= 3 
        
    if N == 0:
        break
    elif N == 1 or N == 2:
        answer = -1
        break
    # print(N)
    # time.sleep(0.5)
print(answer)