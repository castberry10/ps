# 9              			----------> 10 \n 12 \n 11
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1
# 0 1 2 3  4  5 6 7 8
#      1       1
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
answer = [0, 0, 0] # -1 0 1
def cntPaper(x, y, m):
    
    # print('-xym-')
    # print(x,y,m)
    
    cknum = paper[x][y]
    ck = True
    
    if m == 1:
        if cknum == -1:
            answer[0] += 1
            # print('answer[0]')
        elif cknum == 0:
            answer[1] += 1
            # print('answer[1]')
        elif cknum == 1:
            answer[2] += 1
            # print('answer[2]')
        return
    
    for i in range(x, x + m):
        if not ck:
            break
        for j in range(y, y+m):
            if cknum != paper[j][i]:
                ck = False
                break
    
    if ck:#색이 같다면 
        if cknum == -1:
            answer[0] += 1
            # print('answer[0]')
        elif cknum == 0:
            answer[1] += 1
            # print('answer[1]')
        elif cknum == 1:
            answer[2] += 1
            # print('answer[2]')
    else: # 색이 다르다면 
        cntPaper(x, y, m//3)
        cntPaper(x, y+ m//3, m//3)
        cntPaper(x, y+ m//3+ m//3, m//3)
        
        cntPaper(x+ m//3, y, m//3)
        cntPaper(x+ m//3, y+ m//3, m//3)
        cntPaper(x+ m//3, y+ m//3+ m//3, m//3)
        
        cntPaper(x+ m//3+ m//3, y, m//3)
        cntPaper(x+ m//3+ m//3, y+ m//3, m//3)
        cntPaper(x+ m//3+ m//3, y+ m//3+ m//3, m//3)
         

cntPaper(0, 0, n)

for i in answer:
    print(i)
# Test Case 
# 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0