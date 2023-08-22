answer = 0
tempB = 0
dic = {}
dic['A+'] = 4.5
dic['A0'] = 4
dic['B+'] = 3.5
dic['B0'] = 3
dic['C+'] = 2.5
dic['C0'] = 2
dic['D+'] = 1.5
dic['D0'] = 1
dic['F'] = 0


for i in range(20):
    a, b, c = input().split()
    if c == "P":
        continue
    else:
        answer += float(b) * dic[c]
        tempB += float(b)


print(answer / tempB)
