s = input()
n = int(input())
data = list()
answer = 0
for i in range(n):
    a = input()
    for _ in range(len(a)):
        a = a[1:] + a[0]
        
        if s in a:
            answer += 1
            break
print(answer)