import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
                    
answer = 0

for x in range(a):                     
    after = a - x                    
    sleep = b * x                   

    for m in range(n + 1):
        time = 0
        temp_answer = 0
        memo = []               
        for i in t:
            if temp_answer < m and time + a <= i:
                time += a              
                temp_answer += 1
            else:
                memo.append(i)

        if temp_answer < m:        
            continue

        time += sleep

        cnt = temp_answer
        for i in memo:
            if time + after <= i:
                time += after
                cnt += 1

        answer = max(answer, cnt)           

print(answer)
