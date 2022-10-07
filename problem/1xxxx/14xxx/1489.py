N = int(input())

als = list(map(int, input().split()))
bls = list(map(int, input().split()))

# als.sort()
# bls.sort()
# als.reverse()
answer = 0 
# cnt = 0
# for _ in range(N):
#     for i in range(N):
#         for j in range(N):
#             if i > N -1 :
#                 break
#             if als[i] <= bls[j]:
#                 # print('als bls ' , als[i], bls[j])
                
#                 if j - 1 < 0:
#                     break
                
#                 else: 
#                     # print('als bls ' , als[i], bls[j ])
#                     # print('als bls-1 ' , als[i], bls[j -1 ])
                
#                     answer += 2
#                     del als[i]
#                     del bls[j - 1]
#                     N -= 1
#                     # print('alist' , als)
#                     # print('blist' , bls)
                    
#                     break
#                     #als[i] = -1
#                     #bls[j - 1] = -1
#             if als[i] > bls[j] and len(als) == 1 :
#                 answer += 2
#                 break
                

# for _ in range(N):            	
#     for i in range(N):
#         for j in range(N):
#             if i > N - 1:
#                 break
#             if als[i] == bls[j]:
#                 # print('als bls ' , als[i], bls[j])
#                 answer += 1
#                 del als[i]
            
#                 del bls[j]
#                 N -= 1
#                 break

# print(answer)

la = [0 for i in range(1002)]
for i in als:
    la[i] += 1
lb = [0 for i in range(1002)]
for i in bls:
    lb[i] += 1
    
for i in range(1, 1001):
    while la[i]:
        ch = 0
        # print(3)
        for j in range(i-1, 0, -1):
            # print(2)
            if lb[j]:
                ch=1
                answer +=2
                la[i] -= 1
                lb[j] -= 1
                break
                
        if ch == 0:
            break
print(la)
print('--------------')
print(lb)
for i in range(1001):
    while la[i  ] and lb[j ]:
        print(la, lb)
        answer += 1
        la[i ] -= 1
        lb[i ] -= 1
        # print(1)
        
print(answer)
            