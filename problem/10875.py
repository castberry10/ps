# 20230422 미해결
import sys

L = int(input())
N = int(input())
# diri
#   1
# 4   2   // R입력 ->  1 추가
#   3     // L입력 -> -1 추가

# 1 -> y 추가 
# 2 -> x 추가 
# 3 -> y 제거  
# 4 -> x 제거 


data = set()

data.add((0, 0))

x, y = 0, 0
for _ in range(N):
    i, diri = sys.stdin.readline().split()
    i = int(i)
    
    for j in range(1, i + 1):
        
    