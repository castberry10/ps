data = list()
for i in range(8):
    data.append(int(input()))
    
sumanswer = 0
indexanswer = []
for i in range(5):
    maxdata = max(data)
    sumanswer += maxdata
    indexanswer.append(data.index(maxdata) + 1)
    data[data.index(maxdata)] = -1
indexanswer.sort()
print(sumanswer)
print(*indexanswer)