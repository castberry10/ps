from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
n = int(input())
smax = 1
dataset = []
tof = True
answer = ''
for i in range(n):
    tempdataset = int(input())
    while tempdataset >= smax:
        stack.append(smax)
        answer += '+'
        # print('debug +', tempdataset, smax)
        smax += 1
        
    
    a = stack.pop()
    
    if a == tempdataset:
        answer += '-'
        # print('debug -', tempdataset, smax)
    else:
        tof = False
        # print('debug false', tempdataset, smax)
        # break

if tof:
    for i in answer:
        print(i)
else:
    print('NO')