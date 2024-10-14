import heapq

N = int(input())

h = list(map(int, input().split()))
heapq.heapify(h)
for i in range(N - 1):
    d = list(map(int, input().split()))
    for item in d:
        if h[0] < item: 
            heapq.heappop(h)
            heapq.heappush(h, item)
print(heapq.heappop(h))