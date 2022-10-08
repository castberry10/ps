#그리디 문제 
# 5
# 1 1 1 0 2 - > 13
# i, i + 1, i + 2 3개 사면 7원 	2.3
# i, i + 1 2개 사면 5원 		2.5
# i 1개 사면 3원				3.0	
# 당연히 3개 사야 가성비가 좋으나 i+1가 i +2개 보다 많은데도 그렇게사면
# 남은 것들은 연속되지않아서 3.0으로 사야함 
n = int(input())
a = list(map(int, input().split())) #a의 범위는 n 

answer = 0

for i in range(n - 2):
    if a[i + 1] > a[i + 2]:
        min5 = min(a[i + 1] - a[i + 2], a[i])
        
        # print(a, 5, i)
        answer += 5 * min5
        a[i] -= min5
        a[i + 1] -= min5
        
    if a[i] > 0 and a[i + 1] > 0 and a[i + 2] > 0:
        # if a[i + 1] > a[i + 2]:
            
        #     # min5 = min(a[i], a[i + 1])
        #     # print(a, 5, i)
        #     # answer += 5 * min5
        #     # a[i] -= min5
        #     # a[i + 1] -= min5
            
            
                
        min7 = min(a[i], a[i + 1], a[i + 2])
        # print(a, 7, i)
        a[i + 0] -= min7
        a[i + 1] -= min7
        a[i + 2] -= min7
        answer += 7 * min7
    # elif a[i] > 0 and a[i + 1] == 0:
    #     print(a, 3, i)
    #     answer += 3 * a[i]
    #     a[i] = 0
    #     continue

if a[n - 2] > 0:
    if a[n - 1] >0:
        min5 = min(a[n-1], a[n-2])
        # print(a, 5, n-2)
        answer += 5 * min5
        a[n-2] -= min5
        a[n-1] -= min5
# answer += 3 * a[n-1]
# a[n-1] = 0
# answer += 3 * a[n-2]
# a[n-2] = 0

for i in range(n):
    answer += 3 * a[i]
    
# print(a, 3)
print(answer)