# 특별메뉴는 일반메뉴에서 총 20,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 일반메뉴와 특별메뉴에서 총 50,000원 이상을 주문해야 주문할 수 있다.
# 서비스메뉴는 단 하나만 주문할 수 있다.

import sys

A, B, C = map(int, sys.stdin.readline().split())
Ar = dict()
Br = dict()
Cr = set()

Am = 0  # 가격 총합

Bm = 0  # 가격 총합

Cc = 0
for i in range(A):
    d1, d2 = sys.stdin.readline().split()  # 일반메뉴가격
    Ar[d1] = int(d2)
for i in range(B):
    d1, d2 = sys.stdin.readline().split()  # 특별메뉴 가격
    Br[d1] = int(d2)
for i in range(C):
    Cr.add(sys.stdin.readline().rstrip())  # 스페셜메뉴 종류

n = int(input())

for _ in range(n):
    d = input()
    if d in Ar:
        Am += Ar[d]

    elif d in Br:
        Bm += Br[d]

    elif d in Cr:
        Cc += 1

if Cc == 1:  # 스페셜 메뉴가 있니?
    if Bm + Am >= 50000:
        if Bm > 0:
            if Am >= 20000:
                print('Okay')
            else:
                print('No')
        else:
            print('Okay')
    else:
        print('No')
else:
    if Cc > 1:
        print('No')
    elif Bm > 0:  # 이 아래부터는 스페셜 메뉴를 안시킴
        if Am >= 20000:
            print('Okay')
        else:
            print('No')
    else:  # 일반 메뉴만 시킨경우
        print('Okay')
