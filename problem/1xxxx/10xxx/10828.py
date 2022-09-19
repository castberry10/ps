#    / / replit.com

from collections import deque
import sys

# append():- This function is used to insert the value in its argument to the right end of the deque.
# appendleft():- This function is used to insert the value in its argument to the left end of the deque.
# pop():- This function is used to delete an argument from the right end of the deque.
# popleft():- This function is used to delete an argument from the left end of the deque.

N = int(input())
queue = deque()  #popleft, app
for i in range(N):
    data = []
    data = sys.stdin.readline().split(" ")
    data[0] = data[0].strip()
    # print(data)
    if data[0] == "push":
        data[1] = data[1].strip()
        queue.append(data[1])

    elif data[0] == "pop":
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif data[0] == "size":
        print(len(queue))

    elif data[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)

    elif data[0] == "top":
        if queue:
            print(queue[-1])
        else:
            print(-1)
