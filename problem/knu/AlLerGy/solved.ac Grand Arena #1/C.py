t = int(input())

# 다음수가 0이면 먹기

# 만약 양수면 
# 다음수가 양수면 버리기
# 다음수가 음수인데 먹어도 양수면 먹기
# 다음수가 음수인데 먹으면 음수가 되면 버리기 

# 만약 음수면 
# 다음수가 음수면 먹기
# 다음수가 양수인데 먹어도 양수면 먹기 
# 다음수가 양수인데 먹어도 음수면 안먹기

# 만약 0이면 
# 다음수 먹기 

# 지금 내가 바라보고 있는게 마지막수면
# 먹고 끝내거나 
# 안먹고 끝내거나  
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    index = 0
    temp = 0
    pcnt = 0 
    ncnt = 0
    isEat = False
    def tempToZero():
        global temp
        if temp > 0:
            pcnt += 1
        elif temp == 0:
            pass 
        else:
            ncnt += 1
        temp = 0 
    while True:
        if index == n - 1: # 내가 보는게 마지막이면
            pass
        
        if index >= n: # 끝나면
            tempToZero()
            break
        
        # 내가 보고있는게 일반화가 가능하면 
        if temp > 0: # 내가 양수면
# 다음수가 양수면 버리기
# 다음수가 음수인데 먹어도 양수면 먹기
# 다음수가 음수인데 먹으면 음수가 되면 버리기 
            if a[index] > 0:
                break
        elif temp == 0:
            pass
        else: 
            pass
        
    if not isEat:
        if a[len(a)-1] > 0:
            pcnt += 1
        elif a[len(a)-1] == 0:
            pass
        else:
            ncnt += 1
    if pcnt > ncnt:
        print('YES')
    else:
        print('NO')
    
for i in range(t):
    solve()