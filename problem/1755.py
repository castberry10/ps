numstring = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
# print(numstring)

a, b = map(int, input().split())
data = list(map(str, range(a, b + 1)))

def sortkey(x):
    
    a = ""
    if len(x) == 1:
        a += numstring[x]
    else:
        a += numstring[x[0]] + numstring[x[1]] 
    return a
    
data.sort(key = sortkey)

cnt = 0
for i in data:
    cnt += 1
    if cnt % 10 == 0:
        print(i)
    else:
        print(i, end = ' ')