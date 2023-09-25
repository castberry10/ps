data = input('사과, 바나나, 포도 중 선택하세요 : ')
dic = dict()
dic['사과'] = 'apple'
dic['바나나'] = 'banana'
dic['포도'] = 'grape'
if data in dic:
    print(dic[data])
else:
    print('사전에 없는 과일입니다')