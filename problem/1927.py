import heapq
import sys
# 최소힙 문제 
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 
N = int(input())
ls = []
answer = '' #debug
for i in range(N):
    
    a = int(sys.stdin.readline())
    if a == 0:
        if ls:
        	print( heapq.heappop(ls))
            
        else:
            print(0)
            
    else:
        heapq.heappush(ls, a)
