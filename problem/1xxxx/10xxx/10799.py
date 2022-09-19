data = input()

answer = 0
stack = 0

for i in range(len(data)):
    ready = False
    if data[i] == '(':
        if data[i + 1] == '(':
            stack += 1
        else:
            # ready = True
            answer += stack
    else:
        # if ready == True:
        if data[i - 1] == '(':
            # answer += stack
            pass
        else:
            stack -= 1
            answer += 1 
    print("stack", stack)
    print("answer", answer)
    
print(answer)
    

# print(data)