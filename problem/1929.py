import sys
a, b = map(int, sys.stdin.readline().split())

def primeCheck(data):
    if data == 1:
        return False
    for i in range(int(data ** 0.5) + 1):
        if data % 1 == 0:
            return False
    return True

for i in range(a , b +1 ):
    if primeCheck(i):
        print(i)