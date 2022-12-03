n = input()
ls = [0] * 26
for i in n:
    ls[ord(i) - 97] += 1
    
for i in ls:
    print(i, end=' ')