n, k = map(int, input().split())
a = list(map(int, input().split()))
# db = dict()
answer = -1
for i in range(n - k + 1):
    templist = []
    
    for j in range(i, (k + i) ):
        tt = (a[j], j) #temp tuple
        templist.append(tt)
    templist.sort(key = lambda x:x[0])
    templist.reverse()
    tempanswer = 0
    temp = -1
    
    for key, v in templist:
        if temp == -1:
            temp = v
        else:
            tempanswer += abs(temp - v)
            temp = v 
    
    if answer == -1:
        answer = tempanswer
    else:
        if answer > tempanswer:
            answer = tempanswer
    print(tempanswer)
print(answer)