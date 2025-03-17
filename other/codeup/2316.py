# n, m =map(int, input().split())
# data = list(map(int, input().split()))

# for i in data:
#     answer = 0
#     for x in range(1, int(i**0.5) + 1):
#         if i % x == 0:
#             answer += 1
#             if x * x != i:   
#                 answer += 1
#     answer += m // i
#     print(answer - 1)

n, m = map(int, input().split())
data = list(map(int, input().split()))

max_val = max(data)  
divisor_count = [0] * (max_val + 1) 

for i in range(1, max_val + 1):
    for j in range(i, max_val + 1, i):
        divisor_count[j] += 1

for i in data:
    divisors = divisor_count[i]
    multiples = m // i
    print(divisors + multiples - 1)
