N, M = map(int, input().split())
#N에서 M만ㅋㅡㅁ 뽑는다 
#1 1 < 4 2 
#1 2 . . . 
 # 중복상관 O
answer = []
def bt(cnt):
    # 2 2  > 
    # 1 1 1 2 2 1 2 2 > 
    if cnt  == M:
        a = ''
        for i in answer:
        	a += str(i) + ' '
        print(a)
        return
	    
    for i in range(1, N + 1):
        
        if i not in answer:
            answer.append(i)
            bt(cnt + 1)
            answer.pop()
bt(0)