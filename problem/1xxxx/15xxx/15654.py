N, M = map(int, input().split())
A = list(map(int , input().split()))
A.sort()
#N에서 M만ㅋㅡㅁ 뽑는다 
answer = []
def bt(cnt):
    # 2 2  > 
    # 1 1 1 2 2 1 2 2 > 
    if cnt  == M:
        a2 = sorted(answer)
        if a2 != answer:
            return
        a = ''
        for i in answer:
        	a += str(i) + ' '
        
        print(a)
        return
	    
    for i in A:
        
        if i not in answer:
            answer.append(i)
            bt(cnt + 1)
            answer.pop()
bt(0)