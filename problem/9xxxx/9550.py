T = int(input())
for i in range(T):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    answer = 0
    for c in data:
        answer += c // k
    print(answer)