import sys 
import heapq 
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 

# N - 충전 당하는 아이들 수 
# M - 충전을 하는 아이들 수 
N, M = map(int, input().split())
T = list(map(int, input().split()))
T.sort(reverse = True)
# heapq.heapify(T)
answer = []
# if N <= M:
#     pass
# else:
#     pass 

# if len(T) <= M:
#     pass
# else:
#     pass 
for t in T:
    if len(answer) < M:
        heapq.heappush(answer, t)
    else:
        temp = heapq.heappop(answer)
        heapq.heappush(answer, t + temp)
print(max(answer))
