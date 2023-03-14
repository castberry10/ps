max_ = 0
answer = 0
for i in range(1, 6):
    temp = sum((map(int, input().split())))
    if max_ < temp:
        max_ = temp
        answer = i
print(answer, max_)