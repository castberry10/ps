from collections import deque

st = deque()
data = input()

cnt = 0 
answer = ""
for i in range(len(data)):
    if cnt == 0:
        if data[i] == '<': #만약 태그가 시작하면 그동안 모은거를 리버스해서 저장해야함 
            cnt += 1
            while True:
                if len(st) == 0:
                    break
                answer += st.pop()
            answer += data[i]
        else: # 일반 내용
            if data[i] == ' ': #만약 태그가 시작하면 그동안 모은거를 리버스해서 저장해야함 
                while True:
                    if len(st) == 0:
                        break
                    answer += st.pop()
                answer += ' '
            else:
                st.append(data[i])
    else:
        if data[i] == '>': #만약 태그가 끝나면 다시 스택시작
            cnt -= 1
            answer += data[i]
        else: # 그 .. . .. . . .. 태그 내용
            answer += data[i]
while True:
    if len(st) == 0:
        break
    answer += st.pop()
    
print(answer)