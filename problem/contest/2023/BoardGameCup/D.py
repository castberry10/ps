
inputstring = input()
diceList = list(map(int,input().split()))
dice = [0] * 7
for i in diceList:
    dice[i] += 1
answer = 0
if inputstring[0] == "Y":
    tempanswer = (dice[1] + 2) * 1
    if answer < tempanswer:
        answer = tempanswer
if inputstring[1] == "Y":
    tempanswer = (dice[2] + 2) * 2
    if answer < tempanswer:
        answer = tempanswer
if inputstring[2] == "Y":
    tempanswer = (dice[3] + 2) * 3
    if answer < tempanswer:
        answer = tempanswer
if inputstring[3] == "Y":
    tempanswer = (dice[4] + 2) * 4
    if answer < tempanswer:
        answer = tempanswer
if inputstring[4] == "Y":
    tempanswer = (dice[5] + 2) * 5
    if answer < tempanswer:
        answer = tempanswer
if inputstring[5] == "Y":
    tempanswer = (dice[6] + 2) * 6
    if answer < tempanswer:
        answer = tempanswer
if inputstring[6] == "Y":
    tempanswer = 0
    index1 = 0
    index2 = 0
    index3 = 0
    for i in range(7):
        if dice[i] == 1:
            index1 = i
        if dice[i] == 2:
            index2 = i
        if dice[i] == 3:
            index3 = i
    if index1 >= 1 and index2 >= 1:
        tempanswer = max((index1, index2)) * 3 + min((index1, index2)) * 2
    elif index3 >= 1:
        if index3 == 6:
            tempanswer = 6 * 3 + 5 * 2
        else:
            tempanswer = index3 * 3 + 6 * 2        
    
    if answer < tempanswer:
        answer = tempanswer
if inputstring[7] == "Y":
    tempanswer = 0
    indexplus1 = 0
    for i in range(7):
        if dice[i] >= 2:
            indexplus1 = i
    if indexplus1 > 0:
        tempanswer = (dice[indexplus1] + 2) * (indexplus1 - 1)
    else:
        pass
    if answer < tempanswer:
        answer = tempanswer
if inputstring[8] == "Y":
    tempanswer = 0
    cnt = 0
    for i in range(1, 6):
        if dice[i] == 1:
            cnt += 1
    if cnt == 3:
        tempanswer = 30
    if answer < tempanswer:
        answer = tempanswer
if inputstring[9] == "Y":
    tempanswer = 0
    cnt = 0
    for i in range(2, 7):
        if dice[i] == 1:
            cnt += 1
    if cnt == 3:
        tempanswer = 30
    if answer < tempanswer:
        answer = tempanswer
if inputstring[10] == "Y":
    tempanswer = 0
    indexplus1 = 0
    for i in range(7):
        if dice[i] == 3:
            indexplus1 = i
    if indexplus1 > 0:
        tempanswer = 50
    else:
        pass
    if answer < tempanswer:
        answer = tempanswer
if inputstring[11] == "Y":
    tempanswer = sum(diceList) + 12
    if answer < tempanswer:
        answer = tempanswer
print(answer)