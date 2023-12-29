from collections import deque

N, L = map(int, input().split())
deque = deque()
data = list(map(int, input().split()))
for i in range(N):
    while deque and deque[-1][0] > data[i]:
        deque.pop() #계속 빼서 시간복잡도 줄이기 
    deque.append((data[i], i)) # 데이터, 인덱스
    if deque[0][1] <= i - L: #맨 앞에 범위 넘어선건 빼기
        deque.popleft()
    print(deque[0][0], end = ' ')