N = int(input())
ls = list(map(int, input().split()))
ls.sort()
sum1 = 0
if ls[0] >= 2:
    print(1)
    exit() 
# if N == 1:
#     print(ls[0] + 1)
    
for i in range(N):
    sum1 += ls[i]
    if i + 1 == N:
        print(sum1 + 1)
        break
    #index로 부터 안전
    if sum1 >= ls[i +1] or sum1 + 1 == ls[i + 1]:
        continue
    else:
        print(sum1 + 1)
        break
