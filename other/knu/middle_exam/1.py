n, m = map(int, input().split())
data = list(map(int, input().split()))
# data.sort()
start = 0 
end = n - 1
tof = True
while start < end:
    mid = data[start] + data[end]

    if mid == m:
        tof = False
        print(start, end)
        break
    elif mid < m:
        start += 1 
    elif mid > m:
        end -= 1
if tof:
    print(-1)