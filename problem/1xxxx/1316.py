n = int(input())

answer = 0

for i in range(n):
    ck = 0
    data = ""
    a = input()
    for i in range(len(a)):
        if a[i] in data:  # 만약 데이터 중 있다면
            if i == 0:
                pass
            else:
                if a[i] == a[i-1]:
                    pass
                else:
                    ck = 1
        else:  # 만약 데이터 중 없다면
            data += a[i]
    if ck == 1:
        pass
    else:
        answer += 1

print(answer)