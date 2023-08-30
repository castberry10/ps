n = int(input())
a = list(map(int, input().split()))

oddList = []
evenList = []
for i in a:
    if i % 2 == 0:
        evenList.append(i)
    else:
        oddList.append(i)

if len(oddList) == 1 and len(evenList) == 0:
    print(0)
else:
    oddList.sort()
    oddList.reverse()
    maxOddPop = len(oddList) // 2
    oddsum = 0
    for i in range(maxOddPop * 2):
        oddsum += oddList[i]
    # print(evenList)
    # print(oddList)
    
    print(sum(evenList) + oddsum)