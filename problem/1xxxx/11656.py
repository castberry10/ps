data = input()
ls = []
for i in range(len(data) - 1):
    ls.append(data[i:])
ls.sort()

for s in ls:
    print(s)
    