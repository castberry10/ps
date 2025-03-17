n = int(input())
a, b = map(int, input().split())
c = a + b
data = abs(c - n)
data = n - data
answer = '0b' + '1' * data
answer += '0' * (n - (len(answer) - 2))
answer = int(answer, 2)
print(answer)