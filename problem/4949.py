from collections import deque
deque = deque()
while True:
    data = input()
    tof = True
    if data == ".":
        break
    for c in data:
        if c in '({[':
            deque.append(c)
        if c in ')}]':
            if deque:
                a = deque.pop()
                if (a == '(' and c != ')') or (a == '{' and c != '}') or (a == '[' and c != ']'):
                    print('no1')
                    tof = False
                    break
            else:
                tof = False
                print('no2')
                break
    if tof:
        print('yes')
