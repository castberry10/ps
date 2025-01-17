n = int(input())
a = list(map(int ,input().split()))
b = list(map(int, input().split()))
day = 0
datasum = sum(a)
while sum(a) != 0:
    day += 1
    score = [0] * n 
    for i in range(n):
        score[i] = a[i] / b[i]
    maxscore = max(score)
    maxscoreindex = score.index(maxscore)
    b[maxscoreindex] *= 2
    for i in range(n):
        if a[i] != 0:
            if a[i] < b[i]:
                datasum -= a[i]
                a[i] = 0
            else:
                datasum -= b[i]
                a[i] -= b[i]
    b[maxscoreindex] //= 2
print(day)
