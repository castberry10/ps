a = input()
st1 = 0  # 이전이 '(' 라면 -1 ')' 라면 1
st2 = 0
answer = 0
for c in a:
    if c == '(':
        st2 = -1
    else:
        st2 = 1
    
    if st1 == st2:
        answer += 5
    else:
        answer += 10
    
    st1 = st2
print(answer)