import collections
import sys
sys.setrecursionlimit(100000)
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
            return
    state = state % 360 
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
            return
    if K >= A:
        answer += 1
        K -= A
        if K < 0:
            K += A
            return
        if state == 0:
            state = 270 
        else:
            state -= 90
        bt()
        state += 90
        state = state % 360 
        K += A
        answer -= 1
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    if K >= B:
        answer += 1
        K -= B
        if K < 0:
            K += B
            return
        state += 90
        bt()
        state -= 90
        state = state % 360 
        K += B
        answer -= 1
    if K == 0 and state == 0:
        if answer < answercnt:
            answercnt = answer
    if K >= C:
        answer += 1
        K -= C
        if K < 0:
            K += C
            return
        
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

 