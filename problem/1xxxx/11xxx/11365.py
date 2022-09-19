import sys

while True:
    a = sys.stdin.readline().strip()
    if a == 'END':
        break
    print(a[::-1])