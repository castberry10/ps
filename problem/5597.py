ls = [0] * 28
als = []
for i in range(28):
    ls[i] = int(input())

for i in range(1, 30 + 1):
    if i not in ls:
        als.append(i)

als.sort()

print(als[0])
print(als[1])
