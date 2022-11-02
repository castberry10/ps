borad = list()
for i in range(8):
    borad.append(list(input()))
cnt = 0
for i in range(8):
    for j in range(8):
        if borad[i][j] == 'F':
            if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 ==1):
                cnt += 1
print(cnt)