from collections import deque
s = input()
point = 0
startFlag = False
tagname = ""
stack = deque()
endFlag = False
answer = True 
while True:
    if point >= len(s):
        break
    if s[point] == '<':
        startFlag = True
    elif s[point] == '/':
        endFlag = True
    elif s[point] == '>':
        if startFlag and not endFlag: # 여는 태그 
            stack.append(tagname)
        elif startFlag and endFlag:
            if s[point - 1] == "/": # 빈 태그
                pass
            else: # 닫는 태그 
                if stack and stack.pop() == tagname:
                    pass
                else:
                    answer = False
                
        startFlag, endFlag = False, False
        tagname = ""
    else:
        tagname += s[point]
    point += 1

if not stack and answer:
    print("true")
else:
    print("false")