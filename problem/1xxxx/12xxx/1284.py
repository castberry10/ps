while True:
    datas = input()
    if datas == "0":
        break
    answer = 0
    for c in datas:
        if c == '0':
            answer += 4
        elif c == '1':
            answer += 2
        else:
            answer += 3
    answer += len(datas) + 1
    print(answer)