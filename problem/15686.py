# items = ['1', '2', '3', '4', '5']
# from itertools import combinations
# list(combinations(items, 2))
# # [('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
##
# 0은 빈 칸, 1은 집, 2는 치킨집이다.
##
from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
h, c = [], []
# city = []
answer = 10 ** 10

for y in range(n):
    inputlist = list(map(int, input().split()))
    # city.append(inputlist) #생각해보니 필요가 없다 
    for x in range(n):
        if inputlist[x] == 1:
            h.append((y, x))
        elif inputlist[x] == 2:
            c.append((y, x))

# print("h:", h)
# print("c:", c)

for cb in combinations(c, m):
    total = 0 
    # print("cb:", cb)
    for hy, hx in h:
        distance = 10 ** 10
        for cy, cx in cb:
            distance = min(distance, abs(hy - cy) + abs(hx - cx))
        total += distance
    answer = min(answer, total)
print(answer)