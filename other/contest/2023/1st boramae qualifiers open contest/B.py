import sys 

n = int(input())
answer = 0
set_ = set()
for i in range(n):
    id_, value_ = map(int, sys.stdin.readline().split())
    if value_ == 1: #들어가는 기록 
        if id_ in set_:
            answer += 1
        else:
            set_.add(id_)
    elif value_ == 0: # 나오는 기록
        if id_ in set_:
            set_.remove(id_)
        else:
            answer += 1
            
answer += len(set_)
print(answer)