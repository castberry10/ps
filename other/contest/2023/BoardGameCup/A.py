n = int(input())
x = list(map(int, input().split()))
db = list()
tempG = list()#임시 그룹
temp = x[0] - 1
x.sort()
# db.append(list)
answer = 0
cnt = 0 
for i in x:
    # a = i
    
    if i - 1 == temp:#연속일 경우
        tempG.append(i)
        temp = i
        # print("| ",cnt, 1)
    else:#연속이 아닐경우
        db.append(tempG)
        tempG = list()
        # temp = i - 1 temp를 다음수의 -1로 만들어야할텐데
        temp = i
        tempG.append(i)
        # print( "| ",cnt, 0)
    cnt += 1
db.append(tempG)
tempG = list()
# if tempG = [[0], [3,4,5], [8,9]] - > 0 + 3 + 8 
for i in db:
    # print(i)
    answer += min(i)
# print(db)
print(answer)