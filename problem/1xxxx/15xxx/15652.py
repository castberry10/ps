N, M = map(int, input().split())
#N에서 M만ㅋㅡㅁ 뽑는다 
#1 1 < 4 2 
#1 2 . . . 
#4 4 # 중복상관 x 
answer = []
def bt(cnt):
    # 2 2  > 
    # 1 1 1 2 2 1 2 2 > 
    if cnt  == M:
        if sorted(answer) != answer:
            return
        a = ''
        for i in answer:
            
        	a += str(i) + ' '
        print(a)
        return
	    
    for i in range(1, N + 1):
        answer.append(i)
        bt(cnt + 1)
        answer.pop()
bt(0)