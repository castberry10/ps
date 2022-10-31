N, M = map(int, input())
borad = list()
# 012345
# WBWBWB 0
# BWBWBW 1 
# WBWBWB 2

# BWBWBW 0
# WBWBWB 1
# BWBWBW 2 
for i in range(N):
    borad.append(input().split(""))

for c in range(n - 8 + 1):
    for r in range(n - 8 + 1):
        