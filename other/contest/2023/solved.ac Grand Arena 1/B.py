n = int(input())
s = [input() for _ in range(n)]
ss = s.copy()
m = int(input())
a = [input() for _ in range(m)]

qindex = s.index('?')
for word in a:
    tof = True
    s[qindex] = word
    # if word in ss:
    #     tof = False
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                tof=False
                continue
        
    for i in range(n - 1):
        if s[i][-1] != s[i + 1][0]:
            tof = False
    if tof:
        print(word)
        break
