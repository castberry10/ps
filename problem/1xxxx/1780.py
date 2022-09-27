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
        mc = m // 3
        # cntPaper(x, y, mc) # 1
        # cntPaper(x, y+ mc, mc) # 2
        # cntPaper(x, y+ mc+ mc, mc) # 3
        
        # cntPaper(x+ mc, y, mc) # 4 
        # cntPaper(x+ mc, y+ mc, mc) # 5 
        # cntPaper(x+ mc, y+ mc+ mc, mc) # 6
        
        # cntPaper(x+ mc+ mc, y, mc)# 7
        # cntPaper(x+ mc+ mc, y+ mc, mc) # 8 
        # cntPaper(x+ mc+ mc, y+ mc+ mc, mc) # 9
        cntPaper(y, x, mc) # 1
        cntPaper(y, x+ mc, mc) # 2
        cntPaper(y, x+ mc+ mc, mc) # 3
        
        cntPaper(y+ mc, x, mc) # 4 
        cntPaper(y+ mc, x+ mc, mc) # 5 
        cntPaper(y+ mc, x+ mc+ mc, mc) # 6
        
        cntPaper(y+ mc+ mc, x, mc)# 7
        cntPaper(y+ mc+ mc, x+ mc, mc) # 8 
        cntPaper(y+ mc+ mc, x+ mc+ mc, mc) # 9
        return
        # 1 4 7
        # 2 5 8
        # 3 6 9

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