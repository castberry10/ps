while True:
    a = input()
    if a == '#':
        break
    cnt = 0 
    for c in a:
        if c == 'a' or c == 'u' or c == 'e' or c == 'i' or c == 'o':
            cnt += 1
        elif c == 'A' or c == 'U' or c == 'E' or c == 'I' or c == 'O':
            cnt += 1 
    print(cnt)