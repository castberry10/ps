t = int(input())

for i in range(t):
    n = int(input())
    n1 = n + 1
    n100 = n % 100
    if n1 % n100 == 0:
        print('Good')
    else:
        print('Bye')