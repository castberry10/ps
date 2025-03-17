from collections import deque
stack = deque()
n = int(input())

for i in range(n):
    tempinput = int(input())
    if tempinput == 0:
        if stack:
            stack.pop()
            if stack:
                print(stack[-1])
            else:
                print("EMPTY")
        else:
            print("EMPTY")
    else:
        stack.append(tempinput)
        print(stack[-1])
