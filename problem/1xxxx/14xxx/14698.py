import heapq

T= int(input())

for i in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    heapq.heapify(ls)
    answer = 1
    if N == 1:
        print(1)
        continue
    while len(ls) > 1:
        a = heapq.heappop(ls)
        b = heapq.heappop(ls)
        c = a * b
        answer *= c
        heapq.heappush(ls, c)
        # print(ls)
    print(answer % 1000000007)