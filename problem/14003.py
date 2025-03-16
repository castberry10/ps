import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

answer = [data[0]]
dp = [(0, data[0])]

def func2(i):
    start = 0
    end = len(answer) - 1
    while start <= end:
        mid = (start + end) // 2
        if answer[mid] == i:
            return mid
        elif answer[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in data:
    if i > answer[-1]:
        answer.append(i)
        dp.append((len(answer)- 1, i))
    else:
        temp = func2(i)
        answer[temp] = i
        dp.append((temp, i))
        
print(len(answer))
index = len(answer) - 1
answer2 = []

for i in range(len(dp)-1, -1, -1):
    if dp[i][0] == index:
        answer2.append(dp[i][1])
        index -= 1
# print(dp)
answer2 = answer2[::-1]
print(*answer2)