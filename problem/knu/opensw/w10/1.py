a = input()
stack = []
tof = True
for i in a:
    if i == "(":
        stack.append(i)
    elif i == "[":
        stack.append(i)
    elif i == "{":
        stack.append(i)
    elif i == ")":
        if stack:
            if stack.pop() != "(":
                tof = False
        else:
            tof = False
    elif i == "]":
        if stack:
            if stack.pop() != "[":
                tof = False
        else:
            tof = False
    elif i == "}":
        if stack:
            if stack.pop() != "{":
                tof = False
        else:
            tof = False
if tof:
    print("YES")
else:
    print("NO")