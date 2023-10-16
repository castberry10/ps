data = dict()
while True:
    n = int(input('버킷 리스트 메뉴 선택 (1.추가 2.삭제 3.보기 0.종료):'))
    if n == 1:
        k, v = input('사전에 추가할 단어를 입력하세요: ').split()
        data[k] = v
        print(data)
    elif n == 2:
        if len(data) == 0:
            print('사전에 아무것도 없습니다!')
        else:
            s = input('삭제할 단어를 입력하세요: ')
            del data[s]
            print(data)
    elif n == 3:
        print(data)
    elif n == 0:
        print('프로그램을 종료합니다.')
        break
    else:
        print('메뉴 선택 오류입니다. 다시 선택하세요')