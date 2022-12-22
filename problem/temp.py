a = set()
s = input()
for c in s:
    a.add(ord(c))
print(len(s)//len(a))