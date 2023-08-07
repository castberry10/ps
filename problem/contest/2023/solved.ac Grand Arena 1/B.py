n = int(input())
s = [input() for _ in range(n)]
ss = s.copy()
m = int(input())
a = [input() for _ in range(m)]

qindex = s.index('?')
for word in a:
    tof = True
    s[qindex] = word
    if word in ss:
        # print('0', word, s)
        tof = False
        # continue
        
    for i in range(2, n):
        # print('1', s[i-1][-1], s[i][0])
        if s[i-1][-1] != s[i][0]:
            tof = False
    if tof:
        print(word)
        break
