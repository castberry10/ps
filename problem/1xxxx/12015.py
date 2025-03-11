import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

answer = [data[0]]


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
    else:
        temp = func2(i)
        answer[temp] = i
print(len(answer))