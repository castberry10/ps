
# 1 ≤ min ≤ 1,000,000,000,000
# min ≤ max ≤ min + 1,000,000 <- 최대 1,000,000 탐색
import math
MIN, MAX = map(int, input().split())
answer = MAX - MIN + 1 # 탐색 범위
data = [True] * answer

for i in range(2, int(MAX ** 0.5 + 1)):
    squ = i ** 2
    
    
    j = math.ceil(MIN / squ) 
    
    while squ  * j <= MAX:    
        if data[squ * j - MIN] == True:
            data[squ * j - MIN] = False
            answer -= 1
        j += 1

print(answer)
