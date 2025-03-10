N = int(input())


for i in range(N):
    answer = []
    a,b,c = map(int, input().split())
    
    for A in range(1, a+1):
        for B in range(1, b+1):
            for C in range(1, c+1):
                if A % B == B % C == C % A:
                    ls = []
                    ls.append(A)
                    ls.append(B)
                    ls.append(C)
                    ls.sort()
                    if ls not in answer:
                    	answer.append(ls)
    # set_answer = set(answer)
    # print(set_answer) #debug
    # print(len(set_answer))
    # print(answer)
    print(len(answer))
        
        