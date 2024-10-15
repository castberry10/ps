from collections import deque
s = input()
point = 0
answer = True
temptagname = ""
stack = deque()
while True:
    # print(point, len(s))
    # print(stack)
    if point >= len(s):
        break
    if s[point] == "<":
        temptagname = ""
        if s[point + 1] == "/": # 닫는 태그일때 
            point += 1
            while True:
                point += 1
                if s[point] == ">": # 닫는 꺽쇠가 나올때까지
                    if not stack:
                        answer = False
                        point += 1
                        break
                    else:
                        stackpop = stack.pop()
                    if temptagname == stackpop:
                        point += 1
                        break
                    else: # 만약 다르면
                        # print(temptagname, stackpop)
                        # print("여는것과 닫는것이 스택이 다르면")
                        answer = False
                        point +=1 
                        break
                else:
                    temptagname += s[point] 
        else: # 빈 태그이거나 여는태그
            point += 1
            while True:
                if s[point] == ">" or s[point] == " ": #여는태그
                    stack.append(temptagname)
                    if s[point] == ">":
                        point += 1
                    else:
                        while True:
                            if s[point] == ">":
                                point += 1
                                break
                            else:
                                point += 1
                    break
                elif s[point] == "/": # 빈태그
                    point += 2
                    break
                else: 
                    temptagname += s[point]
                    point += 1
                
if answer and not stack:
    print("true")
else:
    print("false")