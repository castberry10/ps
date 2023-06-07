from collections import deque 

stack = deque()

n = int(input())

for i in range(n):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)

print(sum(stack))
        