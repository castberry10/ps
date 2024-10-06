n = int(input())
# mid = 0
# pivot
# min = 
answer = [0, 0, 0]
ls = list(map(int, input().split()))
ls.sort()
min_x = 10 ** 20
# print(ls)
for pivot in range(n):
    start = 0
    end = n-1
    
    while start < end:
        if start == pivot or end == pivot:
            if start == pivot:
                start += 1
                continue
            else:
                end -= 1
                continue
        temp = ls[start] + ls[end]
        # print(ls[start], ls[end], ls[pivot], abs(ls[start] + ls[end] + ls[pivot]))
        if abs(temp + ls[pivot]) < min_x:
            answer = [start, end, pivot]
            min_x = abs(temp + ls[pivot])
            # print(answer,"min", min_x)

        if temp + ls[pivot] < 0:
            start += 1
            # print("start += 1")
        else:
            end -= 1
            # print("end -= 1")
answer.sort()
print(ls[answer[0]], ls[answer[1]], ls[answer[2]])