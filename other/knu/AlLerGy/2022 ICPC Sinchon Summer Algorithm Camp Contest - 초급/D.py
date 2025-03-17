N = int(input())
data = input()

Ls = 0
Ss = 0
answer = 0
for i in data:
    if i in '0123456789':
        answer += 1
    elif i == 'L':
        Ls += 1
    elif i == 'R':
        if Ls:
            Ls -= 1
            answer += 1
        else:
            break
        
    elif i == 'S':
        Ss += 1
    elif i == 'K':
        if Ss:
            answer += 1
            Ss-=1
        else:
            break
        
print(answer)