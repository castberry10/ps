a = input()
n = int(input())
answer = 0
for i in range(n):
    b = input()
    if b == a:
        answer += 1
        
print(answer)