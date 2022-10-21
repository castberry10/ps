N, M = map(int, input().split())
A = list(map(int , input().split()))
A.sort()
#N에서 M만ㅋㅡㅁ 뽑는다 
answer = []
answerlist = set()
def bt(cnt):
    # 2 2  > 
    # 1 1 1 2 2 1 2 2 > 
    if cnt  == M:
        c1 = len(answerlist)
        a = ''
        if answer != sorted(answer):
            return
        for i in answer:
        	a += str(i) + ' '
        
        answerlist.add(a)
        c2 = len(answerlist)
        if c1 == c2:
            return
        print(a)
        return

    for i in A:
        answer.append(i)
        bt(cnt + 1)
        answer.pop()
bt(0)
