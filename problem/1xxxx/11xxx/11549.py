import sys
a = input()
answer = 0
data = sys.stdin.readline().split()
for i in data:
    if i == a:
        answer += 1
print(answer)