import heapq
import sys
input = sys.stdin.readline

minus_h = []
plus_h = []

n = int(input())

answer = 0
zero = False

for i in range(n):
    data = int(input())
    if data == 0:
        zero = True
    elif data == 1:
        answer += 1
    elif data > 0:
        heapq.heappush(plus_h, -1 * data)
    elif data < 0:
        heapq.heappush(minus_h, data)

temp = len(minus_h) // 2

for i in range(temp):
    a = heapq.heappop(minus_h)
    b = heapq.heappop(minus_h)
    c = a * b
    answer += c

temp = len(plus_h) // 2  

for i in range(temp):
    a = heapq.heappop(plus_h)
    b = heapq.heappop(plus_h)
    c = a * b
    answer += c

if minus_h:
    if zero:
        pass
    else:
        a = heapq.heappop(minus_h)
        answer += a

if plus_h:
    a = heapq.heappop(plus_h)
    answer += (-1 * a)

print(answer)