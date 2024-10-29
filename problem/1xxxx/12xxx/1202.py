import heapq
import sys
input = sys.stdin.readline
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 
# 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 
# 가방에는 최대 한 개의 보석만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())
klist = []
nlist = []

for i in range(n):
    heapq.heappush(nlist, list(map(int, input().split())))

for i in range(k):
    klist.append(int(input()))

klist.sort()
answer = 0

temp = []
for i in klist:
    while nlist and nlist[0][0] <= i:
        heapq.heappush(temp, heapq.heappop(nlist)[1] * -1)
    if temp:
        answer += -1 * heapq.heappop(temp)
print(answer)



