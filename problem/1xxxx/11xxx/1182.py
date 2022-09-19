N, S = map(int, input().split())
inputlist = list(map(int, input().split()))
# 5 0 
# -7 -3 -2 5 8
answer = 0
answerlist = []
def dfs(index, sum_):
    global answer
    # print(index, sum_, i)
    if index >=  N:
        return
    
    # if i != 0 and sum_ == S and str_ not in answerlist:
    sum_ += inputlist[index]
    if sum_ == S:
        answer += 1
        #answerlist.append(str_)
            
    # dfs(index + 1, sum_, i, str_)#현재 추가 X
    # # str_ += str(index)
    # dfs(index + 1, sum_ + inputlist[index], i + 1, str_ )#현재 추가
    dfs(index + 1, sum_ - inputlist[index])
    dfs(index + 1, sum_)

# dfs(0, 0, 0, '')
dfs(0, 0)
print(answer)