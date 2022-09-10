n1, n2, n12 = map(int, input().split())
ls = []
ls.append(n1)
ls.append(n2)
ls.append(n12)
ls.sort()
n12 = ls[0]
n1 = ls[1]
n2 = ls[2]
a = (n1 + 1) * (n2 + 1) / (n12 + 1)
print(a - 1)