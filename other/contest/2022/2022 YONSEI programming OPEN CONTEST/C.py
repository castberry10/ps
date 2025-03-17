import sys
n, m = map(int,input().split())
A = list(map(int,sys.stdin.readline().split()))

minM = m
for i in range(n):
    tempM = m
    index = i
    
    while True:
        if tempM < A[index]: #임시 M(사용가능 부피)이 막아야하는 부피보다 작다면
            
            break
        else:#임시 M(사용가능 부피)이 막아야하는 부피보다 크다면 
            tempM -= A[index] 
            if index + 1 >= n:
                break
            index += 1
    if minM > tempM:
        minM = tempM
print(m - minM)
# print(minM)
