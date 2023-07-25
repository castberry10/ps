n, k = map(int, input().split())
set_c = set()
dict_c = dict()
answer = 0
for i in range(n):
    a = int(input())
    if a in set_c:
        dict_c[a] += 1
    else:
        set_c.add(a)
        dict_c[a] = 1
        
for i in set_c:
    if dict_c[i] % k != 0:
        answer = i
        
print(answer)