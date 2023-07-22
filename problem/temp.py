a = 12345
print(a)
print(str(a))
print(map(int, str(a)))
print(sum(map(int, str(a))))
a1, a2, a3, a4, a5 = map(int, str(a))
print(a1, a2, a3, a4, a5)