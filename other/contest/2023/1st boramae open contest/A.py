import sys
sys.setrecursionlimit(10000000)

n = int(input())
x = list(map(int, input().split()))
set_ = set()
# tempset = [0] * (n + 2)
answer = 0
tempanswer = 0
temp = 0
bfsetlen = 0
def bt(cnt):
    global answer
    global temp
    global tempanswer
    
    # print(tempanswer)
    # print(tempset)
    if cnt == n:
        if tempanswer > answer:
            answer = tempanswer
            return
    
    for i in x:
        if cnt == 0: # 첫 선수
            tempanswer = i
            set_.add(i)
            temp = i
            # tempset[0] = i
            bt(cnt + 1)
            set_.remove(i)
            tempanswer = 0
            
            
        else: # 첫 선수가 아니라면 
            bfsetlen = len(set_)
            set_.add(i)
            if len(set_) != bfsetlen: #뭔가 그래도 추가가 됨
                s = i - temp
                if s < 0:
                    s = 0
                tempanswer += s
                ttemp = temp
                temp = i
                # tempset[cnt] = i
                bt(cnt + 1)
                set_.remove(i)
                tempanswer -= s
                temp = ttemp
            else: #추가가 안됨 
                pass
    return
bt(0)
print(answer)