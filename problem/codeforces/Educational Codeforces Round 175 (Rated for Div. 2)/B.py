def f(n, x, k, s):
    answer = 0
    curindex = x
    index = 0
    
    for i in range(k):

        if s[index] == 'L':
            curindex -= 1
        else:
            curindex += 1
            
        index += 1
        
        if curindex == 0:
            answer += 1
            index = 0
        if index == n:
            break
    return answer

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    print(f(n, x, k, s))
