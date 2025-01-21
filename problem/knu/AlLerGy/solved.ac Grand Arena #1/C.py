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

# 지금 내가 마지막수면 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    index = 0
    temp = 0
    pcnt = 0 
    ncut = 0
    while True:
        if index == n - 1:
            pass
        if index >= n:
            if temp > 0:
                pcnt += 1
            elif temp == 0:
                pass
            else:
                ncnt += 1
            break
        if temp > 0:
            pass
        elif temp == 0:
            pass
        else: 
            pass
        
for i in range(t):
    solve()