N = int(input())
nls = list(map(int, input().split()))

ls = [0 for _ in range(1005)]
for i in nls:
    ls[i] += 1
#계수 정ㄹ렬

answer = ''
# print("ls ", ls)
# print()
while N != 0:
    for i in range(1001):
        if N == 0:
            break
        if ls[i] <= 0:
            continue
        else:
            # print("ls ", ls)
            # print()
            if ls[i + 1] <= 0:
                for _ in range(ls[i]):
                    answer = answer + str(i) + ' '
                N -= ls[i]
                ls[i] = 0
                continue
            else:
                cnt = 0
                for j in range(i+2, 1001):
                    if ls[j] > 0:
                        cnt = j
                        break 
                if cnt != 0:
                    for _ in range(ls[i]):
                        answer += str(i) + ' '
                    N-=ls[i]
                    ls[i] = 0
                    answer += str(cnt) + ' '
                    N -= 1
                    ls[cnt] -= 1
                    
                    continue
                else:
                    answer += str(i + 1) + ' '
                    N -= 1
                    ls[i + 1] -= 1
                    continue


print(answer)