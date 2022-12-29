a = input()
ac = 0
bc  = 0
for i in a:
    if i == 'A':
        ac += 1
    else:
        bc += 1
print(ac,':',bc,sep = '')