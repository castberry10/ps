## 틀린 문제 ## 

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
high = set()
lazyhighremove = set()
penalty = [0] * (n+1)
ps = [0] * (n+1)
for _ in range(m):
    a, b = map(int , input().split())
    penalty[a] += b
    ps[a] += 1 
    if a == 1: # 응원하는 팀이 점수 획득
        for i in high:
            if ps[i] < ps[1] or ( ps[i] == ps[1] and penalty[1] < penalty[i]):
                lazyhighremove.add(i)
    else: # 다른팀이 점수 획득
        if ps[a] > ps[1] or (ps[a] == ps[1] and penalty[a] < penalty[1]):
            high.add(a)
        continue
    high -= lazyhighremove
    lazyhighremove = set()
    print(len(high) + 1)
