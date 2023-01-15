import sys
n = int(input())
db = dict()
answer = "NO"
for _ in range(n):
    s, x = sys.stdin.readline().split()
    x = int(x)
    if s in db:  # key가 딕셔너리에 있다면 
        db[s] += x
    else:
        db[s] = x
for k, v in db.items():
    if v == 5:
        answer = "YES"
print(answer)