n, c = map(int, input().split())
dic1 = dict()
dic2 = dict()
dic1['d'] = 'q'
dic1['b'] = 'p'
dic1['q'] = 'd'
dic1['p'] = 'b'
dic2['d'] = 'b'
dic2['b'] = 'd'
dic2['q'] = 'p'
dic2['p'] = 'q'

for i in range(n):
    a = input()
    if c == 1:
        data=""
        for d in a:
            data += dic1[d]
        print(data)
    else:
        data=""
        for d in a:
            data += dic2[d]
        print(data)