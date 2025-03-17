import heapq
n = int(input())
data = list(map(int, input().split()))

if max(data) == min(data):
    print(-1)
else:
    data2 = []
    for i in range(n):
        heapq.heappush(data2, tuple((-1 * data[i], -1 * i)))
    a, b = heapq.heappop(data2)
    print(b * -1)