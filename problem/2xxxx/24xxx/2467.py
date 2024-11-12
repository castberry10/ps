n = int(input())
start = 0
end = n - 1 

ls = list(map(int, input().split()))
answer1 = start
answer2 = end
mix = abs(ls[end] + ls[start])

while start < end:
    mix_temp = ls[end] + ls[start]
    if mix > abs(mix_temp):
        answer1 = start
        answer2 = end
        mix = abs(mix_temp)
    if mix_temp > 0:
        end -= 1
    else:
        start += 1

print(ls[answer1] , ls[answer2])