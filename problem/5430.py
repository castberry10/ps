from collections import deque

import sys
input = sys.stdin.readline
#함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다
T = int(input())

for _ in range(T):
    Rcnt = 0
    p = input().rstrip()
    n = int(input().rstrip())
    xdata = input().rstrip()
    xdata = xdata[1:-1]
    x = list(xdata.split(','))
    xdeque = deque(x)
    if xdata == '':
        xdeque = deque()
    flag = 0
    for c in p:
        
        if flag == -1:
            break
        if c == 'R':
            Rcnt += 1
        else: # c == 'D'
            if len(xdeque) <= 0:
                print('error')
                flag = -1
            else: # xdeque가 비어있지않다. 
                if Rcnt % 2 == 0:
                    xdeque.popleft()
                else:
                    xdeque.pop()
    if flag == -1:
        continue
    x = list(xdeque)
    if Rcnt % 2 == 1:
        x = x[::-1]
    print("["+",".join(x)+"]")