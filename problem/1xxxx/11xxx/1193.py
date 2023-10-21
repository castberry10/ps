x = int(input())
line = 0
m = 0
max_line_n = 0
a = b = 0
while x > max_line_n:
    line += 1
    max_line_n += line
m = max_line_n - x

a = line - m
b = m + 1
if line % 2 == 0:
    print(f'{a}/{b}')
else:
    print(f'{b}/{a}')