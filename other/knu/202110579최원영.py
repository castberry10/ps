def a2xb(a, b, max):
    for i in range(max + 1):
        print(f'{a}x{a}x{i} + {b} = {a ** 2 * i + b}')


a = int(input("a: "))
b = int(input("b: "))
max = int(input("Max: "))

a2xb(a, b, max)