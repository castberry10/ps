n = int(input())
s = input()
data = [0, 0,0,0,0]
for c in s:
    if c == 'H':
        data[0] += 1
    elif c == 'I':
        data[1] += 1
    elif c == 'A':
        data[2] += 1
    elif c == 'R':
        data[3] += 1
    elif c == 'C':
        data[4] += 1
print(min(data))