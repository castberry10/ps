n = int(input())
data = list(map(int, input().split()))
data = set(data)
data = list(data)

data.sort()
oddmin = -1
evenmin = -1

for i in range(n - 1):
    temp = data[i+1] - data[i]
    if temp % 2 == 0:
        if evenmin == -1:
            evenmin = temp
        else:
            evenmin = min(evenmin, temp)
    else:
        if oddmin == -1:
            oddmin = temp
        else:
            oddmin = min(oddmin, temp)
print(evenmin, oddmin)