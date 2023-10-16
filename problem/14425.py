import sys
# input = sys.stdin.readline
n, m = map(int, input().split())
# s = ""
s = set()
answer = 0
for i in range(n):
    # s += input()
    s.add(input())
data = list()

for i in range(m):
    if input().rstrip() in s:
        answer += 1
print(answer)
    
