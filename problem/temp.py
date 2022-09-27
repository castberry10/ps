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
                mc = m // 3
                cntPaper(i, j, mc) # 1
                cntPaper(i, j+ mc, mc) # 2
                cntPaper(i, j+ mc+ mc, mc) # 3
        
                cntPaper(i+ mc, j, mc) # 4 
                cntPaper(i+ mc, j+ mc, mc) # 5 
                cntPaper(i+mc, j+ mc+ mc, mc) # 6
        
                cntPaper(i+ mc+ mc, j, mc)# 7
                cntPaper(i+ mc+ mc, j+ mc, mc) # 8 
                cntPaper(i+ mc+ mc, j+ mc+ mc, mc) # 9
                break
        if not ck:
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
    # else: # 색이 다르다면 
        
    #     return
    #     # 1 4 7
    #     # 2 5 8
    #     # 3 6 9

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