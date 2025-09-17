n = int(input())

mid = n // 2
answer = []

for i in range(mid):
    answer.append(str(mid + 1 + i))    
    answer.append(str(mid - i))      
    

if n % 2 == 1:
    answer.append(str(n))

print(" ".join(answer))
