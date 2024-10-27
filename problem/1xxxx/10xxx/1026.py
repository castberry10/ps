n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()
s = [0] * (n + 2)
for i in range(n):
    s[i] = a[i] * b[i]
    
print(sum(s))