import heapq
import sys
# 최소힙 문제 
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 

# ex 
# heapq.heappush(ls, a)
# heapq.heappop(ls)

N = int(input())
ls = []
answer = 0 

for i in range(N):
    a = int(sys.stdin.readline())
    heapq.heappush(ls, a)

while True:
    if len(ls) == 1:
        break
    a1 = heapq.heappop(ls)
    a2 = heapq.heappop(ls)
    
    a = a1 + a2
    answer += a
    heapq.heappush(ls, a)
print(answer)