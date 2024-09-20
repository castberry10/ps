n = int(input())
data = input()

a = dict()
a['B'] = 0
a['S'] = 0
a['A'] = 0

for i in data:
    a[i] += 1

if a['B'] == a['S'] == a['A']:
    print('SCU')
elif a['B'] == a['S'] and a['S'] > a['A']:
    print('BS')
elif a['B'] == a['A'] and a['A'] > a['S']:
    print('BA')
elif a['A'] == a['S'] and a['S'] > a['B']:
    print('SA')
elif a['S'] > a['A'] and a['S'] > a['B']:
    print('S')
elif a['B'] > a['A'] and a['B'] > a['S']:
    print('B')
elif a['A'] > a['S'] and a['A'] > a['B']:
    print('A')

