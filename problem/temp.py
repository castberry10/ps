# print('1부터 {0}까지의 합은 {1}입니다'.format(n = int(input('정수를 입력하세요 : ')), sum(range(n))))
print((lambda n:f'1부터 {n}까지의 합은 {n*(n+1)//2}입니다.')(int(input('정수를 입력하세요 : '))))
# n = int(input('정수를 입력하세요 : '))
# print('1부터 {0}까지의 합은 {1}입니다'.format(n , sum(range(n+1))))