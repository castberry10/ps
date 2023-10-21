a = input()
b = list(map(int, input().split())) 
b2 = list(map(int, input().split())) 
c = b + b2
c.sort()
print(*c)