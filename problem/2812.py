from collections import deque
# append(): This function is used to insert the value in its argument to the right end of the deque.
# appendleft(): This function is used to insert the value in its argument to the left end of the deque.
# pop(): This function is used to delete an argument from the right end of the deque.
# popleft(): This function is used to delete an argument from the left end of the deque.

queue = deque()

n, m = map(int, input().split())
answer = ''
inputdata = input()
cnt = m
# queue.append(int(inputdata[0]))
# 리버스 큐 제작~~
for s in inputdata:
    ints = int(s)
    while queue and cnt > 0 and int(queue[0]) < ints:
        queue.popleft()
        cnt -= 1
    queue.appendleft(s)

while queue and cnt > 0:
    queue.popleft()
    cnt -= 1
while queue:
    answer += queue.pop()
    
print(answer)
