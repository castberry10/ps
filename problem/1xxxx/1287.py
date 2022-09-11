a = input()
c = 0

ck = 1
for i in range(len(a)):
    if a[i] == '-' or a[i] == '*' or a[i] == '+' or a[i] == '/':
        if i == 0 or len(a) - 1 == i:
            ck = 0
            break
        ckls = ['(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if not ((a[i - 1] in ckls) and (a[i + 1] in ckls)):
            ck = 0
            break
       
if a.find('()') == -1:
    pass
else:
    ck = 0
    
b = a.replace('-', '*')
b = b.replace('+', '*')
try:
    eval(b)
except:
    ck = 0
    
if ck == 1:
    a = a.replace('/', '//')
    try:
        print(eval(a))
    except:
        print('ROCK')
else:
    print('ROCK')