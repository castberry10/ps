N = int(input())
t = list(map(int, input().split()))

t.sort(key = lambda x : -x)

time = 1
# print(t)
answer = 0
for i in t:
    answer = max(answer, time + i)
    time += 1
    
print(answer + 1)