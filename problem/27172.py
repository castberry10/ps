n = int(input())
answerlist = [0] * n

playerCard = list(map(int,input().split())) 
playerCardIndex = {playerCard[i]:i for i in range(n)}

def primef():
    # limit = 1000000 + 1
    # primedata = [True] * (limit)
    # primedata[0] = False
    # primedata[1] = False 
    limit = max(playerCard)
    
    for i in range(n):
        data = playerCard[i]
        for j in range(data * 2, limit+1, data):
            if j in playerCardIndex: # 얘가 마구 나뉘어짐
                answerlist[playerCardIndex[j]] -= 1
                answerlist[i] += 1
primef()
print(*answerlist)
