n = int(input())
data = []
answerdata = [[0 for i in range(n)] for j in range(n)]
numlist = "1234567890"
for i in range(n):
    temp = list(input())
    data.append(temp)

move = [[-1, 0], [0, -1], [1, 0], [0, 1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

#j - m[0], i - y

for i in range(n):
    for j in range(n):
        for m in move:
            if data[i][j] in numlist: #자기 자신이 지뢰면
                answerdata[i][j] = '*'
                break
            if 0 <= j + m[0] < n and 0 <= i + m[1] < n: # 자기 자신이 지뢰가 아니고, index에서 범위를 벗어 나지 않으면 
                if data[i+m[1]][j+m[0]] in numlist: # 체크하는 곳이 숫자 -> 지뢰라면 
                    if answerdata[i][j] == 'M': # 체크한곳이 이미 10개 넘으면 
                        break;
                    answerdata[i][j] += int(data[i+m[1]][j+m[0]])
                    if answerdata[i][j] > 9:
                        answerdata[i][j] = 'M'
                    
for i in range(n):
    for j in range(n):
        print(answerdata[i][j], end="")
    print()
                    
                    