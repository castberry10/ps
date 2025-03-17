dictABC = {}

dictABC['A'] = 4
dictABC['B'] = 3
dictABC['C'] = 2
dictABC['D'] = 1
dictABC['F'] = 0

data = input()

cnt = 0 
score = 0 
for c in data:
    if c in "ABCDF":
        score += dictABC[c]
        cnt += 1
    elif c == '+':
        score += 0.5
print(score / cnt)