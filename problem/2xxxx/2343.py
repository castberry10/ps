n, m = map(int, input().split())
ls = list(map(int, input().split()))
start = max(ls)
end = sum(ls)

while start <= end:
    mid = (start + end) // 2
    box = 1
    cnt = 0
    for i in range(len(ls)):
        if cnt + ls[i] > mid:
            box += 1
            cnt = ls[i]
        else:
            cnt += ls[i]
    if box > m: # 다 못담으면 
        start = mid + 1
    else: # 다 담으면 
        end = mid - 1
print(start)