n = int(input())
for i in range(n):
    data = input()
    ans = 'YES'
    state = 0
    for c in data:
        if c == '(':
            state += 1 
        elif c == ')':
            state -= 1
        if state < 0:
            ans = 'NO'
    if state != 0:
        ans = 'NO'
    print(ans)
        
            