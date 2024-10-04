def primeCheck(data):
    if data == 1:
        return False
    for i in range(2, int(data ** 0.5) + 1):
        if data % i == 0:
            return False
    return True
def palindromeCheck(data):
    data = str(data)
    if data == data[::-1]:
        return True
    else:
        return False
    
n = int(input())

while True:
    n += 1
    if primeCheck(n) and palindromeCheck(n):
        print(n)
        break