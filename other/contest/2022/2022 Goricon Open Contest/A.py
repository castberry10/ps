# 만약 어떤 미션의 계산 금액이 0보다 작은 경우에는 총 금액에 이를 합산하지 않는다

# 만약 어떤 미션의 계산 금액이 0보다 작은 경우에는 총 금액에 이를 합산하지 않는다

# 만약 어떤 미션의 계산 금액이 0보다 작은 경우에는 총 금액에 이를 합산하지 않는다

# 만약 어떤 미션의 계산 금액이 0보다 작은 경우에는 총 금액에 이를 합산하지 않는다

import sys
gamen = int(input())
for _ in range(gamen):
    n = int(sys.stdin.readline())
    answer = 0
    misdata = []
    for _ in range(n):
        misdata.append(list(map(int, sys.stdin.readline().split())))
    k, d, a = map(int, sys.stdin.readline().split())
    for i in range(n):
        K, D, A = misdata[i]
        temp = K * k - d * D + A * a
        if temp < 0:
            temp = 0
        answer += temp 
    print(answer)
    