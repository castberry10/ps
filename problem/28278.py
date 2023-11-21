from collections import deque
import sys

input = sys.stdin.readline
deque = deque()
n = int(input())

for _ in range(n):
    data = input()
    if data[0] == '1':
        a, b= map(int, data.split())
        deque.appendleft(b)
    elif data[0] == '2':
        a, b= map(int, data.split())
        deque.append(b)
    elif data[0] == '3':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif data[0] == '4':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif data[0] == '5':
        print(len(deque))
    elif data[0] == '6':
        print(1 if not deque else 0)
    elif data[0] == '7':
        if deque:
            temp = deque.popleft()
            print(temp)
            deque.appendleft(temp)
        else:
            print(-1)
    elif data[0] == '8':
        if deque:
            temp = deque.pop()
            print(temp)
            deque.append(temp)
        else:
            print(-1)
    