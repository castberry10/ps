# k 줄 각각엔 연산을 나타내는 문자(‘D’ 또는 ‘I’)와 정수 n이 주어진다. 
# ‘I n’은 정수 n을 Q에 삽입하는 연산을 의미한다. 동일한 정수가 삽입될 수 있음을 참고하기 바란다.
# ‘D 1’는 Q에서 최댓값을 삭제하는 연산을 의미하며, ‘D -1’는 Q 에서 최솟값을 삭제하는 연산을 의미한다.
#heapq.heappush(heap, 1)
# print(heapq.heappop(heap))

import heapq
import sys

input = sys.stdin.readline

#  {1 : 2, 2 : 1, 3 : 0}
# it 는 dict 자료형이어야함 
def isEmpty(it):
    for i in it.values():
        if i > 0:
            return False
    return True

T = int(input())
for _ in range(T):
    
    k = int(input())
    min_heap = []
    max_heap = []
    data = dict()
    
    for _ in range(k):
        # print('min', min_heap)
        # print('max', max_heap)
        # print('data',data)
        o, v = input().split()
        v = int(v)
        if o == 'I':
            
            if v in data:
                data[v] += 1
            else:
                data[v] = 1
                heapq.heappush(min_heap, v)
                heapq.heappush(max_heap, -1 * v)
                
        elif o == 'D':
            if isEmpty(data):
                continue
            if v == -1: # 최소힙을 다룹니당 
                while min_heap[0] not in data or data[min_heap[0]] < 1:
                    temp = heapq.heappop(min_heap)
                    if temp in data:
                        del(data[temp])
                data[min_heap[0]] -= 1
            if v == 1: # 최대힙을 다룹니당
                while -1 * max_heap[0] not in data or data[-1 * max_heap[0]] < 1:
                    temp = -1 * heapq.heappop(max_heap)
                    if temp in data:
                        del(data[temp])
                data[-1 * max_heap[0]] -= 1
            
            
    if isEmpty(data):
        print('EMPTY')
    else:
        while min_heap[0] not in data or data[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while -1 * max_heap[0] not in data or data[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        print(-1 * max_heap[0], min_heap[0])