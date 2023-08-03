import math

a, b = map(int, input().split())

answer = math.log10(a) * b
answer = int(answer)

print(answer + 1)