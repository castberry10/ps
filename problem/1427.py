n = input()
l = [0,0,0,0,0,0,0,0,0,0]
for c in n:
    l[int(c)] += 1

for i in range(len(l)):
    for a in range(l[9-i]):
        print(9-i, end = '')