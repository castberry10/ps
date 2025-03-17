import sys
input = sys.stdin.readline

n = int(input())
data = [input().strip() for _ in range(n)]

ck = [[0 for _ in range(i+1)] for i in range(n)]
isSafe = True

for i in range(n-1):
    for j in range(i+1):
        if ck[i][j] == 0:  
            if data[i][j] == 'R' and j <= i and i < n-1 and j+1 <= i+1:
                if data[i+1][j] == 'R' and data[i+1][j+1] == 'R':
                    if ck[i+1][j] == 0 and ck[i+1][j+1] == 0:  
                        ck[i][j] = 1
                        ck[i+1][j] = 1
                        ck[i+1][j+1] = 1
                    else:
                        isSafe = False
                        break
                else:
                    isSafe = False
                    break
            elif j < i and data[i][j] == 'B' and data[i][j+1] == 'B' and data[i+1][j+1] == 'B':
                if ck[i][j+1] == 0 and ck[i+1][j+1] == 0:  
                    ck[i][j] = 1
                    ck[i][j+1] = 1
                    ck[i+1][j+1] = 1
                else:
                    isSafe = False
                    break
            else:
                isSafe = False
                break
    if not isSafe:
        break

if isSafe:
    for i in range(n):
        for j in range(i+1):
            if ck[i][j] == 0:
                isSafe = False
                break
if isSafe:
    print(1)
else:
    print(0)