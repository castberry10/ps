# 피사노 주기를 이용한 풀이
n = int(input())
# cycle = 0
modN = 1000000 # 10^6
cycle = 15 * (10 ** 5)
# print(cycle)
data = [0] * cycle
data[0] = 0
data[1] = 1

for i in range(2, cycle):
    data[i] = (data[i - 1] + data[i - 2]) % modN
    
print(data[n % cycle])