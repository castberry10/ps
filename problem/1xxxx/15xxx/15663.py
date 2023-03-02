N, M = map(int, input().split())
A = list(map(int , input().split()))
A.sort()
#N에서 M만ㅋㅡㅁ 뽑는다 
answer = []
# answerlist = set()
# temp = 0
visit = [False] * (N + 2)
def bt(cnt):
    # global temp
    temp = 0 
    if cnt  == M:
        print(" ".join(map(str, answer))) #  '구분자'.join(리스트)
        return
	    
    for i in range(N):
        if A[i] != temp and visit[i] == False:
            answer.append(A[i])
            temp = A[i]
            visit[i] = True
            bt(cnt + 1)
            answer.pop() #  지정한 위치 값을 삭제하고 삭제한 값 취득 (지정안하면 마지막 인덱스) [1, 2, 3] - > [1, 2]
            visit[i] = False       
        
bt(0)
