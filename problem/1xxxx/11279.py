import heapq
import sys
# 최대힙 문제 
# heapq.heappush(heap, item) : item을 heap에 추가
# heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 IndexError가 호출됨. 
# heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 
N = int(input())
ls = []
answer = '' #debug
for i in range(N):
    # a = int(input()) # 시간 초과 ?? 
    a = int(sys.stdin.readline())
    if a == 0:
        if ls:
            data = heapq.heappop(ls)
            if (data * 10) % 10 == 1:
                print(int(data))
            else:
                print(int(data * -1))
            # answer += str(-1 * heapq.heappop(ls)) + '\n'
        else:
            print(0)
            # answer += '0' + '\n'
    else:
        if a < 0:
            heapq.heappush(ls, float(abs(a)))    
        else:
            heapq.heappush(ls, float(a + 0.1))
        
# print('-----------')
# print(answer)