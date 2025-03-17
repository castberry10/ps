n = int(input())
playerCard = list(map(int,input().split())) 
answerlist = [0] * n
# 0부터 n - 1 플레이어가 존재 
#########################

vsdb = set()

def primeCheck(data):
    if data == 1:
        return False
    for i in range(2, int(data ** 0.5) + 1):
        if data % i == 0:
            return False
    return True

for i in range(n):
    for j in range(n):
        
        if i == j:
            continue
        if i > j:
            a = (j, i)
        else:
            a = (i, j)
        
        if a in vsdb:
            pass
        else:
            vsdb.add(a)
            if playerCard[i] > playerCard[j]:
                if 
            else:
                if playerCard[j] % playerCard[i] == 0:
                    answerlist[i] += 1
                    answerlist[j] -= 1
                else:
                    pass

            # if playerCard[i] > playerCard[j]:
            #     if playerCard[i] % playerCard[j] == 0:
            #         answerlist[i] -= 1
            #         answerlist[j] += 1
            #     else:
            #         pass
            # else:
            #     if playerCard[j] % playerCard[i] == 0:
            #         answerlist[i] += 1
            #         answerlist[j] -= 1
            #     else:
            #         pass

for i in answerlist:
    print(i, end = ' ')
