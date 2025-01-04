def solution(n, info):
    def isWin(a, b): # a가 b를 이기는가 
        # a가 라이언임. 비기는것도 진다고 가정
        # a가 라이언이니 패널티가 있음
        a_score, b_score = 0, 0
        for i in range(11):
            a[i] -= b[i]
            if a[i] > 0:
                a_score += 10-i
            else:
                b_score += 10-i
        return a_score > b_score
    gr_list =[0] * 11
    # 11 - index - 1이 점수..?
    # -점수 + 1 - 11 이 인덱스?
    sort_table = []
    answer = [0] * 11
    for i in range(11):
        score = (11-1-i) / (info[i] + 1)
        gr_list[i] = [(11-1-i), score, info[i] + 1] # 이게 높을 수록 맞추면 이득
    gr_list.sort(key=lambda x : (-x[1], x[0]))
    # 자체 스코어 오름차순
    for i in gr_list:
        if n == 0:
            break
        score, l, count = i[0], i[1], i[2]
        print(answer)
        print('score, l, count', score, l, count)
        if n < count:
            continue
        else:
            answer[10 - score] = count
            n -= count
            
    if isWin(answer, info):
        return answer
    else:
        return [-1]
    
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))