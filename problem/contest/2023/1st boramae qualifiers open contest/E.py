import collections
A, B, C, K = map(int, input().split())
state = 0 # 90 180 270 360 [% 360] 
# j = list(A, B, C)
answer = 0
answercnt = 1000000
def bt():
    global answercnt
    global state
    global answer
    global A
    global B
    global C
    global K
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    state = state % 360 
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    if K >= A:
        answer += 1
        K -= A
        if state == 0:
            state = 270 
        else:
            state -= 30
        bt()
        state += 30
        state = state % 360 
        K += A
        answer -= 1
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    if K >= B:
        answer += 1
        K -= B
        state += 30
        bt()
        state -= 30
        state = state % 360 
        K += B
        answer -= 1
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    if K >= C:
        answer += 1
        K -= C
        state += 180
        bt()
        state -= 180
        state = state % 360 
        K += C
        answer -= 1
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer

bt()

if answercnt == 1000000:
    print(-1)
else:
    print(answercnt)

 