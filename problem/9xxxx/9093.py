import sys
n = int(input())

for i in range(n):
    data = list(sys.stdin.readline().rstrip().split())
    answer = ""
    for s in data:
        s = list(s)
        s.reverse()
        answer += ''.join(s) + ' '
    print(answer)

